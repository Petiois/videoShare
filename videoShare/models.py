# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import  User


class Document(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    docfile = models.FileField(upload_to='files')

    def getDocfile(self):
        return self.docfile.name


    def __unicode__(self):
        return (self.docfile.name)

