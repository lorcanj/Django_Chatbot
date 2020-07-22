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
        #error_list.append(error.__str__())
        error_list.append(error)
    return error_list


def printErrors(input):
    for i in range(len(input.Message)):
        print("Problem: " + input.Message[i].Subject)
        print("Solution to fix: " + input.Message[i].Description)

def returnProof(input):
    proof = ""
    for i in range(len(input.Proof)):
        for j in range(len(input.Proof[i].UsedAxioms.Axiom)):
            proof += input.Proof[i].UsedAxioms.Axiom[j] + "\n"
    return proof

def printProof(input):
    print("That is correct.")
    for i in range(len(input.Proof)):
        for j in range(len(input.Proof[i].UsedAxioms.Axiom)):
            print(input.Proof[i].UsedAxioms.Axiom[j])

def returnWhyNot(input):
    return input.WhyNot[0].Word

def checkAnswerType(answer):
    if (checkForOutput(answer) == "Message"):
        return returnErrors(answer)
    elif (checkForOutput(answer) == "Proof"):
        return returnProof(answer)
    elif (checkForOutput(answer) == "WhyNot"):
        return returnWhyNot(answer)

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