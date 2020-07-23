from suds.client import Client

class AttemptoError:
    def __init__(self, error_subject, error_description):
        self.error_subject = error_subject
        self.error_description = error_description

    def __str__(self):
        return (f"{self.error_subject} and {self.error_description}")

# need to finish this
class AttemptoProof:
    def __init__(self, axiom, used_axiom):
        #need to finish this off
        print("Check line 15")

def createClient():
    url = "http://attempto.ifi.uzh.ch/race_files/race.wsdl"
    client = Client(url)
    return client

def proveStatement(axiom, theorm, client):
    answer = client.service.RunRace(axiom, theorm, "prove")
    return answer

def checkForOutput(input):
    dictionary = Client.dict(input)
    for item in dictionary:
        if (item == "Message"):
            return "Message"
        elif (item == "Proof"):
            return "Proof"
        elif (item == "WhyNot"):
            return "WhyNot"
    return "Error"

def returnErrors(input):
    error_list = []
    for i in range(len(input.Message)):
        error = AttemptoError(input.Message[i].Subject, input.Message[i].Description)
        error_list.append(error)
    return error_list

def printErrors(input):
    for i in range(len(input.Message)):
        print("Problem: " + input.Message[i].Subject)
        print("Solution to fix: " + input.Message[i].Description)

# need to update this with the proof class to make it easier to output
# to the screen
def returnProof(input):
    proof = []
    for i in range(len(input.Proof[0].UsedAxioms.Axiom)):
        proof.append(input.Proof[0].UsedAxioms.Axiom[i])
    return proof

"""
def returnProof(input):
    proof = ""
    for i in range(len(input.Proof)):
        for j in range(len(input.Proof[i].UsedAxioms.Axiom)):
            proof += input.Proof[i].UsedAxioms.Axiom[j] + "\n"
    return proof
"""

def printProof(input):
    print("That is correct.")
    for i in range(len(input.Proof)):
        for j in range(len(input.Proof[i].UsedAxioms.Axiom)):
            print(input.Proof[i].UsedAxioms.Axiom[j])

def returnWhyNot(input):
    return input.WhyNot[0].Word

def checkAnswerType(answer):
    # here is where the ACE text is not correctly formed
    if (checkForOutput(answer) == "Message"):
        return ("Message", returnErrors(answer))
    # here is where the ACE text is formed and correct semantic deduction
    elif (checkForOutput(answer) == "Proof"):
        return ("Proof", returnProof(answer))
    # here is correct syntax but not correct semantics
    elif (checkForOutput(answer) == "WhyNot"):
        return ("WhyNot", returnWhyNot(answer))

## below was created for testing the output
def main():
    client = createClient()
    axiom = "Every man is a human. Every woman is a human. Mary is a woman. John is a man."
    print(axiom)
    theorm = input("Please enter a true statement: \n")
    # theorm = input("Enter an axiom: \n")
    answer = proveStatement(axiom, theorm, client)
    if (checkForOutput(answer) == "Message"):
        printErrors(answer)
    elif (checkForOutput(answer) == "Proof"):
        printProof(answer)
    elif (checkForOutput(answer) == "WhyNot"):
        # doing this because cannot save the value as a string otherwise, however is jank
        print("The following cannot be proved: ")
        # This will only run through once so not too bad for a loop
        for item in answer.WhyNot[0]:
            print(item)

if __name__ == "__main__":
    main()