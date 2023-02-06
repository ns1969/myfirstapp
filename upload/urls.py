from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.run,name='remder'),
    path('fileupload',views.fileup,name='fileupload'),
    path('scriptrun',views.srun,name='scriptrun'),
    path('download',views.downl,name='download'),
]