from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def descubremas1(request):
    return render(request, 'Descubremas1.html')
    
def descubremas2(request):
    return render(request, 'Descubremas2.html')

def descubremas3(request):
    return render(request, 'Descubremas3.html')

def descubremas4(request):
    return render(request, 'Descubremas4.html')
