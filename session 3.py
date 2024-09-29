#list()
courses = ['Introduction to Programming','calculus I','data structures and algorithm','linear algebra','physics I','chemistry I','biology I','microeconomics','macroeconomics','psychology','history I','english composition I','introduction to psychology','calculus II','discrete mathematics']
print(courses)
#sort()
sorted_courses= sorted(courses)
print(sorted_courses)
#reverse()
sorted_courses.reverse()
print(sorted_courses)

count = 1
for item in sorted_courses:
    print (f"course no {count} is {item}" )
    count = count +1
    
courses.reverse()
print(courses)
count = 1
for item in courses:
    print(f"course no{count} is {item}")
    count = count +1
courses.reverse()
print(courses)
#sort()
courses.sort()
print(courses)
courses.reverse()
print(courses)

#1
courses = ['discrete mathematics', 'calculus II', 'introduction to psychology', 'english composition I', 'history I', 'psychology', 'macroeconomics', 'microeconomics', 'biology I', 'chemistry I', 'physics I', 'linear algebra', 'data structures and algorithm', 'calculus I', 'Introduction to Programming']
print(courses)
sorted_courses= sorted(courses)
print("the following courses are available for your interest if you meet the criteria of the courses; ", sorted_courses)
#2
print("one of the courses has been withdrawn and will be replaced by a new course")
print("the old courses were;", courses)
new_courses = ['discrete mathematics', 'calculus II', 'introduction to psychology', 'english composition I', 'history I', 'psychology', 'macroeconomics', 'microeconomics', 'biology I', 'chemistry I', 'physics I', 'linear algebra', 'computer program', 'calculus I', 'Introduction to Programming']
print("the new revised list of courses are;", new_courses)
#3
print("three new courses are introduced" )
new_courses.insert(0, "human science")
new_courses.insert(7, "animal science")
new_courses.append("environment science")
print(new_courses)
#4
print(f"{new_courses[3]},{new_courses[5]},{new_courses[7]},{new_courses[13]} courses will removed due to shortage of technical equipment and space")
new_courses.pop(3)
new_courses.pop(5)
new_courses.pop(7)
new_courses.pop(13)
print("the available courses are:",new_courses)
print("the courses thats no longer available are:introduction to psychology,history I,animal science,linear algebra")
#tuples and loops
#1
courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics"),
    (6, "Chemistry I"),
    (7, "Biology"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]
print(courses)
course_names = []
for course_id, course_name in courses:
    course_names.append(course_name)
    print(course_names)
    #conditional statement
    #A
    course_department = [
        (1,"computer science"),
        (2,"mathematics"),
        (3,"computer science"),
        (4,"mathematics"),
        (5,"physics"),
        (6,"chemistry"),
        (7,"biology"),
        (8,"economics"),
        (9,"economics"),
        (10,"psychology"),
        (11,"history"),
        (12,"english"),
        (13,"psylogy"),
        (14,"mathematics"),
        (15,"computer science"),
        ]
    print(course_department)
    #loop
    while True:
        user_input = input("Enter a course ID (1-15) or type 'quit' or '0' to exit: ").strip()

    if user_input.lower() == 'quit' or user_input == '0':
        print("Exiting the program.")
        break
        
    #conditional statement
    if user_input == course_department
    print("course_department")
    else,
    print("the course ID is not found")
    #search department
    if user_input == [1-15]
    print("course ID []is in the [] department")
    eif user_input == [0-quit]
    print("course ID is out of range, please type in from 1-15 or 0 or quit if you want to quit")
else:
    print("the variable [0] has been used to exit]")
    
    
    
