class Circle:
    # CLASS OBJECT ATTRIBUTE 
    pi = 3.14 

    def __init__(self,radius = 1):
        self.radius = radius

    def area_of_circle(self):
        return self.radius * self.radius * Circle.pi



# creating object 
circle1 = Circle(radius= 12)
print(circle1.area_of_circle())