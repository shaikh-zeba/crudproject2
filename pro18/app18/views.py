
from django.shortcuts import render,redirect
from .forms import *





def home(request):
    return render(request,"home.html")


def stform(request):
    if request.method=="POST":
        obj=StudenttForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={
            "form1":StudenttForm
        }
    return render(request,"stform.html",d)


def stdetails(request):
    data=Student.objects.all()
    d={
        "data":data
    }

  
    return render(request,"stdetails.html",d)


from .forms import CollegeeForm                                                   
def cgform(request):
    if request.method=="POST":
        obj=CollegeeForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d={
            "form":CollegeeForm
        }

        return render(request,"cgform.html",d)
    
def cgdetails(request):
    data=College.objects.all()
    d={
        "data":data
    }

    return render(request,"cgdeatails.html",d)

# def  del1(request):
#     uid=request.GET.get("id")
#     obj=Student.objects.get(id=uid)
#     #write here model class name
#     obj.delete()
#     return redirect("/stdetails")


def del2(request,uid):
    obj=Student.objects.get(id=uid)
    obj.delete()
    return redirect("/stdetails") 


def update(request,uid):
    obj=Student.objects.get(id=uid)
    if request.method=="POST":
        obj=StudenttForm(request.POST,instance=obj)
        #this line is use for upadte data
        obj.save()
        return redirect("/stdetails")
    else:
        d={
            "form1":StudenttForm(instance=obj)
            #fill data in form
        }

        return render(request,"stform.html",d)

def add(request,uid):
    obj=Student.objects.get(id=uid)
    if request.method=="POST":
        obj=StudenttForm(request.POST)
        #this line is use for upadte data
        obj.save()
        return redirect("/stdetails")
    else:
        d={
            "form1":StudenttForm
             #fill data in form
        }

        return render(request,"stform.html",d)   
    
     
def srch(request):
    return render(request,"home.html")

# create change here  


