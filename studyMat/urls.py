from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('ee', views.ee, name='ee'),
    path('ce', views.ce, name='ce'),
    path('me', views.me, name='me'),
    path('cse', views.cse, name='cse'),
    path('csedd', views.csedd, name='csedd'),
    path('ece', views.ece, name='ece'),
    path('ecedd', views.ecedd, name='ecedd'),
    path('mat', views.mat, name='mat'),
    path('chem', views.chem, name='chem'),
]