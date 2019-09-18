from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/accounts/login')
    return response