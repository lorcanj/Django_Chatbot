from django.http import HttpResponse
from django.shortcuts import render

from .models import Puzzle

# Create your views here.
def index(request):
    return render(request, "puzzle_app/index.html", {
        "puzzles": Puzzle.objects.all()
    })

def puzzle(request, puzzle_id):
    puzzle = Puzzle.objects.get(pk=puzzle_id)
    return render(request, "puzzle_app/puzzle.html", {
        "puzzle": puzzle
    })

