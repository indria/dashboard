from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render

def dash(request):
    return render(request, 'dash/dash.html')