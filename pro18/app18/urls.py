from django.urls import path
from .import views as v

urlpatterns = [

    path('',v.home),
    path('stform',v.stform),
    path('stdetails',v.stdetails),
    path('cgform',v.cgform),
    path('cgdetails',v.cgdetails),
    # path('del1',v.del1),
    path("del2/<int:uid>",v.del2),
    path("update/<int:uid>",v.update),
    path("add/<int:uid>",v.add),
    path("srch",v.srch)
   
 
]