from suds.client import Client

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

def printErrors(input):
    for i in range(len(input.Message)):
        print("Problem: " + input.Message[i].Subject)
        print("Solution to fix: " + input.Message[i].Description)

def printProof(input):
    print("That is correct.")
    for i in range(len(input.Proof)):
        for j in range(len(input.Proof[i].UsedAxioms.Axiom)):
            print(input.Proof[i].UsedAxioms.Axiom[j])

def printWhyNot(input):
    print(input.WhyNot[0].Word)

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