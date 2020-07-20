from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .Attempto import *
from .models import Puzzle

class GuessForm(forms.Form):
    guess = forms.CharField(label="User Guess", min_length=1)

# Create your views here.
def index(request):
    return render(request, "puzzle_app/index.html", {
        "puzzles": Puzzle.objects.all()
    })

def puzzle(request, puzzle_id):
    puzzle = Puzzle.objects.get(pk=puzzle_id)
    if request.method == "GET":
        return render(request, "puzzle_app/puzzle.html", {
            "puzzle": puzzle, "form": GuessForm()
        })
    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data["guess"]
            client = createClient()
            axiom = puzzle.text
            theorm = guess
            answer = proveStatement(axiom, theorm, client)
            response = checkAnswerType(answer)
            return HttpResponse(response)
        else:
            return render(request, "puzzle_app/puzzle.html", {
            "puzzle": puzzle, "form": form
        })

def guess(request):
    if request.method == "POST":
        guess = request.POST
        return HttpResponse("Hello")



