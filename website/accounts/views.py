from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from  django.core.urlresolvers import reverse
# Create your views here.
def home(request):
    numbers=[1,2,3,4,5]
    name="UTKARSH"
    args={'myName':name,'numbers':numbers}
    return render(request,'home/home.html',args)

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')    
    else:
        form =RegistrationForm()
        args={'form':form}
        return render(request,'accounts/reg_from.html',args)    
@login_required
def profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user    
    args={'user':user}
    return render(request,'accounts/profile.html',args)
@login_required
def edit_profile(request):
    if request.method=='POST':
        form =EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:edit_profile'))
      
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)
@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
             form.save()
             update_session_auth_hash(request,form.user)
             return redirect(reverse('accounts:profile'))
        else:
            return redirect(reverse('accounts:change_password'))    
     
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)
