class Person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
p1=Person("linus",30,"oslo","Norway")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)