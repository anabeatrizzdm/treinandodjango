from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response

def say_hello(request):
    return render(request, 'hello.html')

def imagem(request):
    return render(request, 'imagem.html')
