from django import forms
from django.http import HttpResponse, Http404
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
    try:
        puzzle = Puzzle.objects.get(pk=puzzle_id)
    except Puzzle.DoesNotExist:
        raise Http404("Puzzle not found")
    if request.method == "GET":
        return render(request, "puzzle_app/puzzle.html", {
            "puzzle": puzzle, "form": GuessForm()
        })
    
    # need to change the variable names from theorm and axiom as not clear

    # need a variable here to check the response type to then properly create the UI for the output
    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            guess = form.cleaned_data["guess"]
            client = createClient()
            axiom = puzzle.text
            theorm = guess
            answer = proveStatement(axiom, theorm, client)
            responses = checkAnswerType(answer)
            answer_type = responses[0]
            response_text = responses[1]
            return render(request, "puzzle_app/output.html", {
                "response_text" : response_text, "puzzle":puzzle, "answer_type": answer_type
            })
            
        else:
            return render(request, "puzzle_app/puzzle.html", {
            "puzzle": puzzle, "form": form
        })