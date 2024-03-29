# -*- coding: utf-8 -*-
from django.contrib.auth.models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from videoShare.models import Document
from videoShare.forms import DocumentForm
from videoShare.settings import MEDIA_ROOT
from hashlib import sha256
import os
import datetime
from django.db import IntegrityError



def home(request):
    Liste=[]
    documents = Document.objects.all()
    count=0
    try:
        for document in documents:
            if count<10:
                Liste.append(document)
                count += 1
    except Document.DoesNotExist:
        return redirect('/list')
    return render_to_response('home.html',{'Liste':Liste},context_instance=RequestContext(request))

def isLog(request):
   login = request.user.username
   password = request.user.password
   return HttpResponse(("Login = %s\n"%login,"\nPassword = %s"%password))

def custom404(request):       
   return HttpResponse("ERREUR 404")
   
@login_required
def list(request):
    # Load documents for the list page
    documents = Document.objects.filter(author=request.user)
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

@login_required
def detail(request, offset):

    if request.method == 'POST':
        temp = Document.objects.get(id=offset)
        docPath = temp.getDocfile()
        Document.objects.filter(id=offset).delete()
        path = MEDIA_ROOT+'/'+docPath
        os.remove(path)
        return HttpResponseRedirect('/list')
    else:
        try :
            temp = Document.objects.get(id=offset)
            docPath = temp.getDocfile()
            videoPath = '/media/' + docPath
            path = MEDIA_ROOT+'/'+docPath
            offset = int(offset)
            doc = Document.objects.filter(id=offset)
            if request.user==doc.get(id=offset).author:
                varBool=True
            else:
                varBool=False
            return render_to_response(
                'detail.html',{'doc':doc, 'varBool':varBool,'videoPath':videoPath },context_instance=RequestContext(request)
            )
        except Document.DoesNotExist:
            return redirect('/list')
        except ValueError:
            raise custom404()

@login_required
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            temp = Document(docfile = request.FILES['docfile'])
            newdoc = Document(
                author = request.user,
                name = temp.docfile.name,
                date = datetime.datetime.now(),
                docfile = temp.docfile
            )
            m = sha256()
            m.update(newdoc.docfile.read())
            newdoc.docfile.name = m.hexdigest()+os.path.splitext(newdoc.docfile.name)[1]
            newdoc.save()
            return redirect('/list')
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

@login_required
def profile(request):
    profile = User.objects.get(username=request.user.username)
    test = profile.last_name
    if request.method == 'POST':
        User.objects.filter(username=request.user.username).delete()
        return HttpResponseRedirect('/')
    return render_to_response('registration/profile.html',{'profile':profile},context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    wrongTyping = False
    noUserName = False
    if request.method == 'POST': 
         login = request.POST['login']
         password = request.POST['password']
         password2 = request.POST['password2']
         name = request.POST['name']
         surname = request.POST['surname']
         if (login == '') :
            noUserName = True
            return render(request, 'registration/newuser.html', { 'noUserName' : noUserName , 'name' : name , 'surname' : surname
            })
         if (password2 != password or password2 =='' or password =='') :
            wrongTyping = True
            return render(request, 'registration/newuser.html', { 'wrongTyping' : wrongTyping ,'login' : login
            })
         try:
            new_user = User.objects.create_user(login,None,password)
            new_user.first_name = surname
            new_user.last_name = name
            new_user.save()
            return HttpResponseRedirect('/')
         except IntegrityError:
            accountAlreadyCreated = True
            return render(request, 'registration/newuser.html', { 'accountAlreadyCreated' : accountAlreadyCreated, 'name' : name , 'surname' : surname
            })
    else:
     #   form = ContactForm() # An unbound form
        return render(request, 'registration/newuser.html', {
        })

def stream(request, offset):
    temp = Document.objects.get(id=offset)
    docPath = temp.getDocfile()
    videoPath = '/media/' + docPath
    path = MEDIA_ROOT+'/'+docPath
    return render_to_response(
        'stream.html',{'videoPath':videoPath },context_instance=RequestContext(request)
    )
