class student:
    def __init__(self,name, grade):
        self.name=name
        self.grade=grade
s1= student("Anna","A")
print(s1.grade)
s1.grade="B"
print(s1.grade)