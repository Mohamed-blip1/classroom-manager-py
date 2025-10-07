# manage_student_flow.py
max_grad=20.0
min_grad=0.0


def add_(classroom)->bool:
    
    name=input("Enter student name: ")
    if classroom.student_exist(name):
        print("Error: Student already exist!!")
        return False
    
    grade=float(input(f"Enter '{name}' grade: "))
    if not classroom.grade_valid(grade):
        print(f"Error: -Max grade: {max_grad} | -Min grade: {min_grad} !!")
        return False
    
    if not classroom.add_student(name,grade):
        print("Error: classroom.add_student()!! .")
        return False
    
    print("Seccuss adding!")
    
    return True

def remove_(classroom)->bool:

    name=input("Enter student name: ")
    if not classroom.student_exist(name):
        print("Error: Student name does not exist!!")
        return False
    
    if not classroom.remove_student(name):
        print("Error: classroom.remove_student()!!")
        return False 
    
    print("Seccuss removing!")
    return True