from django.db.models import Max
from django.test import Client, TestCase

# problem when using client class from suds and django
#import suds
#from .Attempto import *
from .models import Puzzle


# Create your tests here.

class PuzzleTestCase(TestCase):

    def setUp(self):

        # A valid puzzle
        p1 = Puzzle.objects.create(description="This is a test description.", text="There is a man.")

        #Non-valid due to lack of full stop
        p2 = Puzzle.objects.create(description="Another test", text= "There is a man")

        #Non-valid due to not syntatically correct ACE
        p3 = Puzzle.objects.create(description="One more test case", text="Hello plums.")

    def test_index(self):
        c = Client()
        response = c.get("/puzzle_app/")
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["puzzles"].count(), 3)
    

    def test_valid_puzzle_page(self):
        p = Puzzle.objects.get(description="This is a test description.")
        c = Client()
        response = c.get(f"/puzzle_app/{p.id}")
        self.assertEqual(response.status_code, 200)

    
    def test_invalid_puzzle_page(self):
        max_id = Puzzle.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"/puzzle_app/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    
class AttemptoTestCase(TestCase):
    """
    def test_errorReturn(self):
        client = suds.client.Client("http://attempto.ifi.uzh.ch/race_files/race.wsdl")
        answer = proveStatement("There is a woman.", "There is a woman.", client)
        print(type(answer))
        self.assertTrue(len(answer) > 0)
    """


