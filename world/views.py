from django.shortcuts import render

# Create your views here.

def world_index(request):
    return render(request, "world_index.html")