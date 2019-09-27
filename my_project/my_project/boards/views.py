from django.shortcuts import render
from django.http import HttpResponse
from .models import Board


# Create your views here.
def home(request):
    board_objects = Board.objects.all()
    return render(request, 'home.html', {'boards': board_objects})
