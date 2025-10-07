# student.py
class Student:
    
    def __init__(self,name,grade):
        self.__name=name
        self.__grade=grade

    @property
    def name(self):
        return self.__name
    @property
    def grade(self):
        return self.__grade