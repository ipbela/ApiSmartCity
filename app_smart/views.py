from django.shortcuts import render
from django.http import HttpResponse

def abre_index(request):
    mensagem = "Olá Turma!"
    return HttpResponse(mensagem)

def cad_user(request):
    return render(request, 'Cad_User_Api.html')