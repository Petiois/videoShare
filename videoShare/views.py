from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def custom404(request):
    return HttpResponse("404")

