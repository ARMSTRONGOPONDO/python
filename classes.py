class location:
    def __init__ (self, country ,name):
        self.name=name
        self.country=country
    def mylocation(self):
        print("My name is "+ self.name + " and I currently live in "+ self.country +" and I will be travelling to the states by the end of 2026")
loc1 = location("KENYA","Omuhinda")
loc2 = location("New york", "Armstrong")
loc3 = location("UK","Opondo")
loc1.mylocation()
loc2.mylocation()
loc3.mylocation()
