class Student:
    first_name = ""
    last_name = ""
    age = 0
    average_score = 0.0
    isPayed = True

#st = Student ()
#for item in dir(st):
for item in dir(Student):
    if(not item.startswith("__")):
        print(item, type(getattr(Student, item)))
