from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render

def subs(request):
    return render(request, 'subs/subs.html')