# Program #5: Course Info
# Henry Forst
#Week 8 programs
#10/24/2025
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
def course_info():
    courses = {}
    while True:
        course_id = input("Enter a course ID or 'done' to be finished: ")
        if course_id == 'done':
            break
        course_name = input("Enter a course name: ")
        courses[course_id] = course_name
    subject = input("Enter a subject such as 'COS': ")
    print(f'Courses for subject {subject}: ')
    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f'{course_id}: {course_name}')
            found = True
    if not found:
        print("No courses found for the subject entered.")
course_info()