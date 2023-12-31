from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisteration
from .models import User

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            rm = fm.cleaned_data['rollno']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
        reg = User(name=nm,rollno=rm,email=em,password=pw)
        reg.save()
        return render(request, 'enroll/success.html', {'nmm':nm})
        # fm = StudentRegisteration()    
            
    else:
        fm = StudentRegisteration() 
        stud = User.objects.all()   
        return render(request, 'enroll/addandshow.html', {'form':fm , 'stu':stud} )
        
    #for delete 
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)  
        pi.delete()
        return HttpResponseRedirect("/")  
    
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            #it is short cut 
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(instance=pi)
            
        
    return render(request, 'enroll/updatestudent.html', {'form':fm})


# Create your views here.
