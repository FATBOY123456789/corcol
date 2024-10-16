class Circle:
    def __init__(self):
        self.radius=float(input('Enter the radius of circle: '))
    def area(self):
        areasum=3.14*self.radius
        return areasum
    def perimeter(self):
        perimetersum=2*3.14*self.radius
        return perimetersum
c1=Circle()
print('Area of circle is: ',c1.area(),'and perimeter of circle is: ',c1.perimeter())