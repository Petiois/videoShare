# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from videoShare.models import Document
from videoShare.forms import DocumentForm
from django.http import HttpResponse
from hashlib import sha256
import os.path
import datetime


def home(request):
   return HttpResponse("Home Page")

def isLog(request):
   login = request.user.username
   password = request.user.password
   return HttpResponse(("Login = %s\n"%login,"\nPassword = %s"%password))

def custom404(request):       
   return HttpResponse("ERREUR 404")
   
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            temp = Document(docfile = request.FILES['docfile'])
            newdoc = Document(
                    author = request.user.username,
                    name = temp.docfile.name,
                    date = datetime.datetime.now(),
                    docfile = temp.docfile
                )
            #newdoc = Document(docfile = request.FILES['docfile'])
            m = sha256()
            m.update(newdoc.docfile.read())
            newdoc.docfile.name = m.hexdigest()+os.path.splitext(newdoc.docfile.name)[1]
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('videoShare.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

