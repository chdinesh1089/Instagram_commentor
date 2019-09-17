from django.shortcuts import render
from .models import Page
from .tasks import run_monitoring
from celery import uuid
from Insta_Comment.celery import app
from django.core import serializers
from .python_scripts.comments_bot import start_monitoring
# Create your views here.
def monitoring(request):
    pages_list = Page.objects.all()
    context = {
        'pages_list': pages_list,
    }
    current_user = request.user
    current_user = current_user.username
    #current_user = serializers.serialize('json', request.user)
    if (request.method == 'POST' and 'run_cmnts' in request.POST):
        from .python_scripts import test
        rqst = request.POST
        task_id = uuid()
        #if 'stop_cmnts' in x:
        #print(x['stop_cmnts'])
        account_id = rqst['run_cmnts']
        account_object = Page.objects.get(account_id = account_id)
        account_object.task_id = task_id
        account_object.run_status = "yes"
        account_object.save()
        #start_monitoring(account_object)
        #test.testu()
        #print(task_id)
        run_monitoring.apply_async(args=[account_id,current_user],task_id=task_id)

    elif (request.method == 'POST' and 'stop_cmnts' in request.POST):
        from .python_scripts import test
        rqst = request.POST
        task_id = uuid()
        #if 'stop_cmnts' in x:
        #print(x['stop_cmnts'])
        account_id = rqst['stop_cmnts']
        account_object = Page.objects.get(account_id = account_id)
        app.control.revoke(account_object.task_id)
        account_object.task_id = 'na'
        account_object.run_status = "no"
        account_object.save()
        #run_monitoring.apply_async(args=[account_id],task_id=task_id)
    return render(request, 'commentbot/monitoring.html', context)

