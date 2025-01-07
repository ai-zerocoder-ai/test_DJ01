from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>data</h1>")

def test(request):
    return HttpResponse("<h1>test</h1>")
