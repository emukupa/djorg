from django.shortcuts import render
from . models import Note
# Create your views here.


def index(request):
    context = {"notes": Note.objects.all()}
    return render(request, 'notes/index.html', context)
