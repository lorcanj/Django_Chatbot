from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .Attempto import *
from .models import Puzzle


# Create your views here.
def index(request):
    return render(request, "puzzle_app/index.html", {
        "puzzles": Puzzle.objects.all()
    })

def puzzle(request, puzzle_id):
    if request.method == "GET":
        puzzle = Puzzle.objects.get(pk=puzzle_id)
        return render(request, "puzzle_app/puzzle.html", {
            "puzzle": puzzle
        })
    if request.method == "POST":
        guess = request.POST.get("user_guess")
        client = createClient()
        axiom = "There is a man."
        theorm = guess
        answer = proveStatement(axiom, theorm, client)
        return HttpResponse(answer)

def guess(request):
    if request.method == "POST":
        guess = request.POST
        return HttpResponse("Hello")



