class Circle:
    def __init__ (self, radius):
        self.radius = radius

    def circumfrence(self):
        pi =3.14
        circumfrencevalue = 2 * self.radius *pi
        return circumfrencevalue

    def printcurmfrence(self):
        circumfrence = self.circumfrence()
        print("the circumfrence radius is " + str(self.radius) +" and the value of circle is  " + str(self.circumfrence) + "as string")

circl1 = Circle(7)
circl1 = Circle(8)
circl1.printcurmfrence()
circl1.printcurmfrence()
