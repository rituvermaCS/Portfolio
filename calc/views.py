from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from calc.models import Contact

# Create your views here.

def index(request):
     return render(request,'index.html')
     
def about(request):
     return render(request,'about.html')          
     
def skill(request):
     return render(request,'skill.html')     
     
def contact(request):
     if request.method=='POST':
         name=request.POST['name']
         msg=request.POST['msg']
         contact_data=Contact(name=name,msg=msg)
         contact_data.save()
         messages.success(request,"Your Messege have been send Successfully.")
         return redirect('contact')
     else:
         return render(request,'contact.html')      