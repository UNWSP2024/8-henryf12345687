# Program #3: Capital Quiz
# Henry Forst
#Week 8 programs
#10/24/2025
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random
def capital_quiz():
    states = {"Montana": "Helena","Wisconsin": "Madison", "Nevada": "Carson City", "Michigan": "Lansing","Minnesota": "St.Paul"}
    correct_count = 0
    incorrect_count = 0
    state_list = list(states.keys())
    random.shuffle(state_list)
    for state in state_list[:5]:
        guess_Cap = input(f"What is the capital of {state}?:").strip()
        if guess_Cap == states[state]:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect. The capital of {state} is {states[state]}")
            incorrect_count += 1
    print(f"You have completed the quiz! You got {correct_count} correct and {incorrect_count} incorrect.")
capital_quiz()