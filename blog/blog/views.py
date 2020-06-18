from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Olá Mundo!")

def vai(request):
    return HttpResponse("Vai da certo nessa porra ")