from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from django.template.response import TemplateResponse
from django.contrib import messages
from .models import myuploadfile
from django.http import HttpResponseRedirect
import os
import mimetypes
def run(request):
    return(render(request,'home.html'))

def fileup(request):
    if request.method =='post':
        myfiles=request.FILES.getlist('myfiles')
        if len(myfiles)<3:
            c=0
            s=[]
            s=list(map(str,myfiles))
            for i in range(len(s)):
                if '.xlsx' in s[i] and '.csv' in s[i]:
                    if 'ource' in s[i] or 'arget' in s[i]:
                        c=c+1
            if c<2:
                messages.info(request,'Wrong Format')
                return HttpResponse('/')
            if c==2:
                for fil in myfiles:
                    my_uploadedfiles=myuploadfile(myfiles=fil)
                    my_uploadedfiles.save()
                messages.info(request,'Files Uploaded')
                return HttpResponse('/')
        else:
            messages.info(request,'More then two files')
            return HttpResponse('/')

def srun(request):
    df_csv=pd.read_csv(r'media/source.csv')
    out_path=('media/target.xlsx')
    writer=pd.ExcelWriter(out_path,engine='xlsxwriter')
    df_csv.to_excel(writer,index=False,header=False)
    writer.save()
    return(render(request,'home.html'))

def downl(request):
    BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename='target.xlsx'
    filepath=BASE_DIR+'/media'+filename
    path=open(filepath,'rb')
    mime_type,=mimetypes.guess_type(filepath)
    response=HttpResponse(path,content_type=mime_type)
    response['Content-Disposition']="attachment;filename=%s"%filename
    return response
