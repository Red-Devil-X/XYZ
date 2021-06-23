class Car(object):
    def __init__(self,modal,speedlimit,color,company):
        self.modal=modal
        self.speedlimit=speedlimit
        self.color=color
        self.company=company

    def carstart(self): 
        print("car started" + self.color)

    def carstop(self):
        print("car stopped")

    def changegear(self):
        print("change gear")

Swift = Car("Dezire","500","white","Swift")
print(Swift.color)
Swift.carstart()


Honda = Car ("light","900","black","Tata")
print(Honda.modal)
Honda.changegear()
