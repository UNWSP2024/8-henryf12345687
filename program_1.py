# Henry Forst
#Week 8 programs
#10/24/2025
# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator():

    personsName = input('Enter the users first, middle, and last name: ')
    #    Add your logic here
    initials = personsName.split()
    for string in initials:
        print(string[0].upper(),sep='',end='')
        print('.',sep = '', end = '')
initials_generator()
