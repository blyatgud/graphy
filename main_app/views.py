from django.shortcuts import render
from .models import Graphy

def index(request):
	musico = Graphy.objects.all()
	return render(request, 'index.html', {'musico': musico})