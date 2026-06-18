class rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
r1= rectangle(5,3)
print(r1.area())
