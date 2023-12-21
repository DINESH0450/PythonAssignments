class Car:
    def __init__(self,brand,mileage,color,isAutometic):
        self.brand= brand
        self.mileage=mileage
        self.color=color
        self.isAutometic=isAutometic
    
    def show_features(self):
        print(self.brand)
        print(self.mileage)
        print(self.color)
        print(self.isAutometic)
        if self.isAutometic==True:
            print("Its Autometic")
        elif self.isAutometic==False:
            print("Its Manual")
        else:
            print("give valid input")
CarObj1=Car("Honda",25,"blue",False)     
CarObj2=Car("Creta",20,"white",True)  

CarObj1.show_features()
CarObj2.show_features()

