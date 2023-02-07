from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from .models import myuploadfile
from django.http import HttpResponseRedirect
import os
import mimetypes
from django.core.files import File
def run(request):
    return(render(request,'home.html'))

def fileup(request):
    if request.method =='POST':
        myfiles=request.FILES.getlist('myfiles')
        if len(myfiles)<3:
            c=0
            s=[]
            s=list(map(str,myfiles))
            for i in range(len(s)):
                if '.xlsx' in s[i] or '.csv' in s[i]:
                    if 'ource' in s[i] or 'arget' in s[i]:
                        c=c+1
                        print(c)
            if c<2:
                messages.info(request,'Wrong Format')
                return HttpResponseRedirect('/')
            if c==2:
                for fil in myfiles:
                    my_uploadedfiles=myuploadfile(myfiles=fil)
                    my_uploadedfiles.save()
                messages.info(request,'Files Uploaded')
                return HttpResponseRedirect('/')
        else:
            messages.info(request,'More then two files')
            return HttpResponseRedirect('/')

def downl(request):
    BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename='source.csv'
    filepath =BASE_DIR + '/media/' + filename
    path=open(filepath,'rb')
    mime_type,_=mimetypes.guess_type(filepath)
    response=HttpResponse(path,content_type=mime_type)
    response['Content-Disposition']="attachment;filename=%s"%filename
    return response
