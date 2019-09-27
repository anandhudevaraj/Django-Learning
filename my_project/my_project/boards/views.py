from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board


# Create your views here.
def home(request):
    board_objects = Board.objects.all()
    return render(request, 'home.html', {'boards': board_objects})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
