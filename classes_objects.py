class student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return f"verygood{self.name}"
        else:
            return False
        
        
student1 = student(name = " rahim", gpa= 3.2)
student2 = student(name = " ali wzir", gpa= 3.8)

print(student2.on_honor_roll())

print(student1.gpa)
print(student2.name)


        