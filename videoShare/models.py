# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import  User


class Document(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    date = models.DateField()
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __unicode__(self):
        return u'%s %s' % (self.name)

