# filing.py
import json

def enter_(classroom)->bool:
    choice=input("would you like to LOAD previous data? (enter) or [y/n] :> ")

    if choice=='n' or choice=='N':
        return False

    with open("students.json","r") as file:
        data=json.load(file)
        
        if len(data)==0:
            return False
        
        for name,grade in data.items():
            classroom.add_student(name,grade)
    return True

def exit_(classroom)->bool:

    if classroom.students_len==0:
        return False

    choice=input("would you like to SAVE new data? (enter) or [y/n] :>")

    if choice=='n' or choice=='N':
        return False

    with open("students.json","w") as file:
        json.dump({n: s.grade for n,s in classroom.students_items},file,indent=4)
    return True

def clear_():

    with open("students.json","w") as file:
        json.dump({},file)