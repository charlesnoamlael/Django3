from django.shortcuts import render


def hello_blog(request):
    lista = [ 'Charles', 'Noam', 'Lael', 'Edvania']
    
    data = {'name': 'Curso de Django 3', 'lista_tecnologia' : lista}
    
    return render(request,'index.html', data)

