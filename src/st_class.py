# st_class.py
import student

class Class:

    def __init__(self,class_id):
        self.__class_name=int(class_id)
        self.__students={}
        self.__max_grade=20.0
        self.__min_grade=0.0
        self.__grades_sum=0.0
    
    @property
    def grades_sum(self):
        return self.__grades_sum
    @property
    def students_len(self):
        return len(self.__students)
    @property
    def students_val(self):
        return self.__students.values()
    @property
    def students_items(self):
        return self.__students.items()

    def student_exist(self,name:str)->bool:
        return name in self.__students
    
    def grade_valid(self,grade:float)->bool:
        return grade>=self.__min_grade and grade<=self.__max_grade

    def add_student(self,name:str,grade:float)->bool:
        if self.student_exist(name) or not self.grade_valid(grade):
            return False
        
        self.__students[name]=student.Student(name,grade)
        self.__grades_sum+=grade
        return True
    
    def remove_student(self,name)->bool:
        if not self.student_exist(name):
            return False
        # self.__students.pop(name) I did use this before I check the function you shared with me
        self.__grades_sum-=self.__students[name].grade
        del self.__students[name]
        return True