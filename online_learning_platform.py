class person:
    def __init__(self, person_id, name, age):
        self.person_id=person_id
        self.name=name
        self.age=age
    def display_person_info(self):
        print(f"person_id:{self.person_id}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
class student(person):
    def __init__(self, person_id, name, age,course_name, course_fee):
        super().__init__(person_id, name, age)
        self.course_name=course_name
        self.course_fee=course_fee
    def calculate_discount(self):
        discount=self.course_fee*10/100
        final_fee=self.course_fee-discount
        return final_fee
    def display_student_info(self):
        super().display_person_info()
        print(f"cousre name:{self.course_name}")
        print(f"course fee:{self.course_fee}")
class programmingstudent(student):
    def __init__(self,person_id,name, age,course_name, course_fee,programming_language,project_count):
        super().__init__(person_id, name, age, course_name, course_fee)
        self.programming_language=programming_language
        self.project_count=project_count
    def calculate_discount(self):
        discount=self.course_fee*20/100
        final_fee=self.course_fee-discount
        return final_fee
    def display_programmingstudent_info(self):
        super().display_student_info()
        print(f"programming language:{self.programming_language}")
        print(f"project count:{self.project_count}")
s1= student(101,"Dev",19,"Bca", 84000)
s2= student(102,"Prince",18,"Btech",90000)
s3= student(103,"Saurab",20,"Bca",84000)
p1= programmingstudent(101,"disha",21,"Bca",100000,"Python","AI model")
p2=programmingstudent(102,"jai",21,"Bca",95000,"C++","Graph analyser")
s1.display_student_info()
s2.display_student_info()
s3.display_student_info()
p1.display_programmingstudent_info()
p2.display_programmingstudent_info()


        
