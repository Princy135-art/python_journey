class cat:
    def sound(self):
        print("Meow")
class fox:
    def sound(self):
        print("wa-pa-pa-pa")
c1=cat()
f1=fox()
for animal in (c1,f1):
    animal.sound()