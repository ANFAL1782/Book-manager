from django.urls import path,include
from.import views
from django.conf import settings

urlpatterns = [
    path('',views.Index,name='Home'),
    path('About/',views.About,name='About'),
     path('Teachers/',views.TeachersPage,name='Teachers'),
    path('Registor/',views.Registor,name='Registor'),
   path('Books/',views.Bookpage,name='Books'),

    path('Contact/',views.Contact,name='Contact'),
   
]
