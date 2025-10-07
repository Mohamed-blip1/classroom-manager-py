# main.py
from enum import Enum
import manage_student_flow
import st_class
import utils
import stats
import filing

class Menu(Enum):
    Add='a'
    Remove='r'
    Stats='s'
    List='l'
    Menu='m'
    Clear='c'
    Exit='e'

classroom=st_class.Class(1)
filing.enter_(classroom)

utils.menu()
while True:

    choice=input(">")
    match choice:

        case Menu.Exit.value:
            filing.exit_(classroom)
            print("Goodbey!")
            break

        case Menu.Menu.value:
            utils.menu()

        case Menu.Add.value:
            if not manage_student_flow.add_(classroom):
                print("Failed to add student!!")

        case Menu.Remove.value:
            if not manage_student_flow.remove_(classroom):
                print("Failed to remove student!!")

        case Menu.Stats.value:
            if not stats.stats_(classroom):
                print("No students were added!!")
        
        case Menu.List.value:
            if not stats.list_(classroom):
                print("No students were added!!")

        case Menu.Clear.value:
            filing.clear_()
            print("Success clearing!")

        case _:
            print(f"'{choice}' not a valid choice!!")
            continue
