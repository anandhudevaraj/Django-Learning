from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Board, Topic, Post


# Create your views here.
def home(request):
    board_objects = Board.objects.all()
    return render(request, 'home.html', {'boards': board_objects})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']

        user = User.objects.first()  # TODO

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics', pk=board.pk)  # TODO - Redirect to created topic page

    return render(request, 'new_topic.html', {'board': board})
