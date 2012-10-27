# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django import *
from django.contrib.auth.models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import *
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
    return render_to_response('home.html',context_instance=RequestContext(request))

def isLog(request):
   login = request.user.username
   password = request.user.password
   return HttpResponse(("Login = %s\n"%login,"\nPassword = %s"%password))

def custom404(request):       
   return HttpResponse("ERREUR 404")
   
@login_required
def list(request):
    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )


def detail(request, offset):
    try :
        offset = int(offset)
    except ValueError:
        raise custom404()
    doc = Document.objects.filter(id=offset)
    if request.user.username==doc.get(id=offset).author:
        varBool=True
    else:
        varBool=False
    #import pdb; pdb.set_trace()
    return render_to_response(
        'detail.html',{'doc':doc, 'varBool':varBool}
    )

def upload(request):
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
            return redirect('/')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render_to_response(
        'upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def secu(request,offset):
    return

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST': 
        toto = request.POST['sender']
        tata = request.POST['message']
        User.objects.create_user(toto,None,tata)
        return HttpResponse(toto+tata)
# If the form has been submitted...
       # form = ContactForm(request.POST) # A form bound to the POST data
       # if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
        #    return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
     #   form = ContactForm() # An unbound form

        form = 2
        return render(request, 'registration/newuser.html', {
           'form': form,
        })


