from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return HttpResponse('Website Page!')

def login_redirect(request):
        return redirect('/account/login')