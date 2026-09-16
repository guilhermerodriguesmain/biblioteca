from django.shortcuts import render
from django.http import HttpResponse

def inicio(requests):
    return HttpResponse("Funcionou")
