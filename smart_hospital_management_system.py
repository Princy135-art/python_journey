class person:
    def __init__(self,person_id,name,age):
        self.person_id=person_id
        self.name=name
        self.age=age
    def display_person_info(self):
        print(f"person id:{self.person_id}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
class doctor(person):
    def __init__(self,person_id,name, age,specialization, salary):
        super().__init__(person_id,name,age)
        self.specialization=specialization
        self.salary=salary
    def calculate_bonus(self):
        bonus=self.salary*15/100
        final_salary=self.salary+bonus
        return final_salary
    def display_doctor_info(self):
        super().display_person_info()
        print(f"specialization:{self.specialization}")
        print(f"alary:{self.salary}")
class patient(person):
    def __init__(self,person_id,name,age,disease,treatment_cost):
        super().__init__(person_id,name,age)
        self.disease=disease
        self.treatment_cost=treatment_cost
    def claculate_bill(self):
        bill=self.treatment_cost
        return bill
    def display_patient_info(self):
        super().display_person_info()
        print(f"disease:{self.disease}")
        print(f"treatment cost:{self.treatment_cost}")
class hospitalmember(doctor, patient):
    def __init__(self,person_id,name, age, specialization, salary, disease,treatment_cost,ward_number):
        person.__init__(self,person_id,name, age)
        self.specialization=specialization
        self.salary=salary
        self.disease=disease
        self.treatment_cost=treatment_cost
        self.ward_number=ward_number
    def display_complete_info(self):
        super().display_person_info()
        print(f"specialization:{self.specialization}")
        print(f"salary:{self.salary}")
        print(f"disease:{self.disease}")
        print(f"treatment cost:{self.treatment_cost}")
        print(f"ward number:{self.ward_number}")
d1=doctor(1,"Jai",19,"cardiologist",100000)
p1=patient(2,"Devi",78,"sugar",7000)
h1=hospitalmember(3,"yana",36,"dermatologist",90000,"high bp",9000,23)
d1.display_doctor_info()
p1.display_patient_info()
h1.display_complete_info()
