# Program #2: 
# Henry Forst
#Week 8 programs
#10/24/2025
# Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator():
    user_input = input('Enter a sentence with all the words together and the first letter in each word being capatilized: ')
    new_sentence = user_input[0].upper()
    #    Add your logic here
    for char in user_input[1:]:
        if char.isupper():
            new_sentence += " " + char.lower()
        else:
            new_sentence += char
    new_sentence += "."
    print(new_sentence)

# Example usage

#sentence = "StopAndSmellTheRoses"

#new_sentence = word_separator(sentence)

#print(new_sentence)
word_separator()