class Car(object):
    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        if (self.price >10000):
            self.tax = .15

        else:
            self.tax = .12
        self.speed = speed
        self.fuel = fuel
        if(self.fuel<20):
            self.fuel = "almost Empty"

        elif(self.fuel >= 20 and self.fuel < 10):
            self.fuel = "kinda full"

        else:
            self.fuel = "good enough"
        self.mileage = mileage + " mpg"

    def displayAll(self):
        print "Price: ${}".format(self.price) + " Speed: {}".format(self.speed) + " Fuel: {}".format(self.fuel) + " Mileage: {}".format(self.mileage) + " Tax: {}".format(self.tax)

myCar = Car(2000, 50, 40, '25')
myCar2 = Car(3000, 60, 50, '35')
myCar3 = Car(4000, 70, 60, '45')
myCar4 = Car(5000, 80, 70, '55')
myCar5 = Car(6000, 90, 80, '65')
myCar6 = Car(15000, 100, 90, '75')

myCar.displayAll()
myCar2.displayAll()
myCar3.displayAll()
myCar4.displayAll()
myCar5.displayAll()
myCar6.displayAll()
