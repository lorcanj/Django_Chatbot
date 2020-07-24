from suds.client import Client

class AttemptoError:
    def __init__(self, error_subject, error_description):
        self.error_subject = error_subject
        self.error_description = error_description

    def __str__(self):
        return (f"{self.error_subject} and {self.error_description}")


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

def returnProof(input):
    proof = []
    for i in range(len(input.Proof[0].UsedAxioms.Axiom)):
        proof.append(input.Proof[0].UsedAxioms.Axiom[i])
    return proof

def returnWhyNot(input):
    whyNot = []
    for i in range(len(input.WhyNot)):
        whyNot.append(input.WhyNot[i])
    return whyNot

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
    theorm = "There is a man."
    answer = proveStatement(axiom, theorm, client)
    print(answer)
    
if __name__ == "__main__":
    main()