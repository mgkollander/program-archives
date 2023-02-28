# Function to check if input is valid
def checkInput(lang, statesCount, stateInitial, statesFinal, transitions):
    # Check that number of states is over 0
    if statesCount <= 0:
        return False
    # Check that initial state is over 0 and not bigger than total state count
    if stateInitial < 0 or stateInitial >= statesCount:
        return False
    # Check that final states are greater than 0 and not bigger than total state count
    for state in statesFinal:
        if state < 0 or state >= statesCount:
            return False
    # Check if all states are in table
    for state in range(statesCount):
        if state not in transitions:
            return False
        # Check if all elements are in table
        for element in lang:
            if element not in transitions[state]:
                return False
            if transitions[state][element] < 0 or transitions[state][element] >= statesCount:
                return False
    return True


# Function to gather input for transition table
def handleInput():
    # Gather user input
    lang = input("Enter the language set separated by spaces (Ex. \"a b\"): ").split()
    statesCount = int(input("Enter the number of states (Ex. \"2\"): "))
    stateInitial = int(input("Enter the initial state (Ex. \"0\"): "))
    statesFinal = list(map(int, input("Enter the final state(s) (Ex. \"1\"): ").split()))

    # Create transition table
    transitions = {}
    for state in range(statesCount):
        transitions[state] = {}
        for element in lang:
            transitions[state][element] = -1

    # Gather user input for each transition
    for state in range(statesCount):
        for element in lang:
            nextState = int(input(f"Enter the next state for state {state} and element {element}: "))
            transitions[state][element] = nextState
    
    # Check if inputs are valid
    if not checkInput(lang, statesCount, stateInitial, statesFinal, transitions):
        print("Invalid input")
        return None
    
    return lang, statesCount, stateInitial, statesFinal, transitions


# Function to check user string
def checkString(lang, statesCount, stateInitial, statesFinal, transitions, userString):
    stateCurrent = stateInitial
    for element in userString:
        if element not in lang:
            return "INVALID STRING"
        stateCurrent = transitions[stateCurrent][element]

    if stateCurrent in statesFinal:
        return "ACCEPTED"
    else:
        return "NOT ACCEPTED"

# Main
userInput = handleInput()
# Extract input, gather string, and determine if accepted
if userInput is not None:
    lang, statesCount, stateInitial, statesFinal, transitions = userInput
    userString = input("Enter a string to check: ")
    result = checkString(lang, statesCount, stateInitial, statesFinal, transitions, userString)
    print(result)

# Wait for input
input("Press enter to quit...")