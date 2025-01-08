from django.shortcuts import render

def data(request):
    return render(request, "dj02/data.html")

def data_2(request):
    return render(request, "dj02/data_2.html")

def data_3(request):
    return render(request, "dj02/data_3.html")

def test(request):
    return render(request, "dj02/test.html")
