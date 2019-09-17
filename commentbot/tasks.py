from .python_scripts import comments_bot
from Insta_Comment.celery import app
from django.core.cache import cache

@app.task
def run_monitoring(account_id,current_user):
    comments_bot.start_monitoring(account_id,current_user)
    #cache.set(current_task_id, operation_results)
