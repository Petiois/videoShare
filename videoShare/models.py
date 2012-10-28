# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import  User


class Document(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    date = models.DateField()
    docfile = models.FileField(upload_to='files')

    def getDocfile(self):
        return self.docfile.name

    def getAuthor(self):
        return self.author

    def __unicode__(self):
        return (self.docfile.name)

class ProfileUser(models.Model):
    login = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_connexion = models.CharField(max_length=50)
    register_date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

