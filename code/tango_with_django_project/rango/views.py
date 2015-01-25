from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    #return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
    return render(request, 'rango/index.html', context_dict)
def about(request):
    #return HttpResponse("Rango says here is the about page! <br/> <a href='/rango/'>Rango</a> ")
    context_dict = {'boldmessage': "These are big letters"}
    return render(request, 'rango/about.html', context_dict)