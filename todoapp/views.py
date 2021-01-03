from django.shortcuts import render

# Create your views here.

def home(request):
    diction={}
    return render(request, 'todoapp/index.html', context=diction)