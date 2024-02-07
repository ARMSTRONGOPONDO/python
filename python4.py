class Rectangle:
    def __init__(self,length,width):
        self.width=width
        self.length=length
    
    def area(self):
        rect_area=self.length*self.width
        return rect_area
 
rectangle1=Rectangle(5,9)
print(rectangle1.area())


