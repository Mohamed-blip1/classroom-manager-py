# stats.py
def stats_(classroom)->bool:
    
    if classroom.students_len==0:
        return False
    
    avg=classroom.grades_sum/classroom.students_len
    highest_student=max(classroom.students_val,key=lambda s:s.grade)
    lowest_student=min(classroom.students_val,key=lambda s:s.grade)

    print(f"Class average: {avg:.2f}")
    print(f"Highest grade: {highest_student.name}({highest_student.grade})")
    print(f"Lowest grade : {lowest_student.name}({lowest_student.grade})")
    return True

def list_(classroom)->bool:
    
    if classroom.students_len==0:
        return False
    
    for a,s in classroom.students_items:
        print(f"{a:>12} : {s.grade}")
    return True