# lets Start
list  = []  #List
student = [] 
 
number  = int(input('Number of Students:'))


for elem in range(number):
    name = input('Name of the Student:')
    numerOfSubjects = int(input(' Numer of subjects: '))
    subjects = []    
    for num in range(numerOfSubjects):
        print('subjects:' , num +1)
        subjectsName = input('name of the Subject')
        subjectsGrades = int(input ('Grade of subject'))
        subjects.append((subjectsName,subjectsGrades))
        
    student.append((name, subjects))
    
for part in student:
    name = student[0]
    subjects = student[1]
    print('Name of the Student:',name)
    total = 0 
    for sub in subjects:
        subjectsName = sub[0]
        subjectsGrades = sub[1]        
        print("Name of Subject:",subjectsName,"Grade in Subject",subjectsGrades)
        total += subjectsGrades
    average = total /len(subjects)
    print('avrage Grade:' ,average)
    
    
    
    
    students = []

number = int(input('Number of Students: '))

for _ in range(number):
    name = input('Name of the Student: ')
    number_of_subjects = int(input('Number of subjects: '))
    subjects = []

    for i in range(number_of_subjects):
        print('Subject:', i + 1)
        subject_name = input('Name of the Subject: ')
        subject_grade = int(input('Grade of the Subject: '))
        subjects.append((subject_name, subject_grade))

    students.append((name, subjects))

# Ausgabe
for student in students:
    name = student[0]
    subjects = student[1]
    print('\nName of the Student:', name)
    total = 0

    for subject in subjects:
        subject_name = subject[0]
        subject_grade = subject[1]
        print("  Name of Subject:", subject_name, "Grade in Subject:", subject_grade)
        total += subject_grade

    average = total / len(subjects)
    print('  Average Grade:', average)
