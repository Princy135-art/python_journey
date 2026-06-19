class person:
    def __init__(self, person_id,name,age,**kwargs):
        super().__init__(**kwargs)
        self.person_id=person_id
        self.name=name
        self.age=age
    def display_person_info(self):
        print(f"person id:{self.person_id}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
    def get_role(self):
        return "person"
class student(person):
    def __init__(self,course,sem, fee,**kwargs):
        super().__init__(**kwargs)
        self.course=course
        self.sem=sem
        self.fee=fee
    def calculate_fee(self):
        scholarship=self.fee*10/100
        final_fee=self.fee-scholarship
        return final_fee
    def display_student_info(self):
        super().display_person_info()
        print(f"course:{self.course}")
        print(f"sem:{self.sem}")
        print(f"fee:{self.fee}")
    def get_role(self):
        return "student"
class employee(person):
    def __init__(self,department, salary,**kwargs):
        super().__init__(**kwargs)
        self.department=department
        self.salary=salary
    def calculate_salary(self):
        salary=self.salary*15/100
        final_salary=self.salary+salary
        return final_salary
    def display_employee_info(self):
        super().display_person_info()
        print(f"department:{self.department}")
        print(f"salary:{self.salary}")
    def get_role(self):
        return "employee"
class teachingassistant(student,employee):
    def __init__(self,person_id,name,age,course,sem,fee,department,salary,assigned_lab,attend):
        super().__init__(
            person_id=person_id,
            name=name,
            age=age,
            course=course,
            sem=sem,
            fee=fee,
            department=department,
            salary=salary
        )
        self.assigned_lab=assigned_lab
        self.__attend=attend
    def calculate_fee(self):
        scholarship=self.fee*50/100
        final_fee=self.fee-scholarship
        return final_fee
    def calculate_salary(self):
         salary=self.salary*25/100
         final_salary=self.salary+salary
         return final_salary
    def display_complete_info(self):
        super().display_person_info()
        print(f"course:{self.course}")
        print(f"sem:{self.sem}")
        print(f"fee:{self.fee}")
        print(f"department:{self.department}")
        print(f"salary:{self.salary}")
        print(f"assigned lab:{self.assigned_lab}")
    def get_role(self):
        return "teachingassistant"
    def get_attend(self):
        return self.__attend
    def set_attend(self, attend):
            if 0 <= attend <= 100:
                self.__attend = attend
            else:
                print("Invalid attendance")
s1=student(person_id=101,
           name="dev",
           age=21,
           course="btech",
           sem=5,
           fee=90000)
e1=employee(person_id=1001,
            name="jay",
            age=34,
            department="frontend",
            salary=60000)
ta1=teachingassistant(person_id=101,
                      name="maya",
                      age=45,
                      course="bsc",
                      sem=8,
                      fee=80000,
                      department="fullstack",
                      salary=100000,
                      assigned_lab=501,
                      attend="98")
s1.display_student_info()
e1.display_employee_info()
ta1.display_complete_info()
file = open("people.txt", "r")
for line in file:
    print(line)











