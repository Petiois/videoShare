from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def custom404(request):
    user= request.user.username
    password= request.user.password
    string = "Login : "+user+"\n"+"Password : "+password
    return HttpResponse(string)

