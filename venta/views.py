from django.shortcuts import render

def ventas(request):
    return render(request, 'ventas.html')