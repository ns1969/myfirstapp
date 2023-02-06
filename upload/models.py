from django.db import models

class myuploadfile(models.Model):
    myfiles=models.FileField(upload_to="",null=False,default=None)
