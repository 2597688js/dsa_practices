"""
 A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
Take following input from user
    Number of classes held
    Number of classes attended.

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
"""

def is_allowed_exam(total_classes:int, attended_classes:int)->(float,bool):
    attendance_percentage = (attended_classes / total_classes) * 100
    allowed = False
    if attendance_percentage >= 75:
        allowed = True
    
    return attendance_percentage, allowed


if __name__ == "__main__":
    total_cls = int(input("Number of classes held : "))
    attended_cls = int(input("Number of classes attended: "))
    attendance_prcnt, allowed = is_allowed_exam(total_cls, attended_cls)
    yes_no = ""
    if allowed:
        yes_no = "allowed"
    else:
        yes_no = "not allowed"
        
    print(f"Attendance is : {attendance_prcnt:.4f} % and you are {yes_no} to sit in the exam !!")
