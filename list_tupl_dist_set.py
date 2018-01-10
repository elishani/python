#list
courses = ['History', 'Nath', 'Physics', 'CompSci']

for index, course in enumerate(courses, start=1):
    print("{}. {}" .format( index, course))
print (', '.join(courses))

#Tupl



#set
empty_set = set()

#Dict

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student.get('Phone', 'Not Found'))