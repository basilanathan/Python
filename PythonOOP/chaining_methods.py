class Bike(object):
    def __init__(self, price, speed):
        self.speed= speed
        self.price = price
        self.miles =0
    def displayInfo(self):
        print "{}, {}, {} miles".format(self.speed, self.price, self.miles)
        return self
    def riding (self, amount=1):
        self.miles += 10 * amount
        print "I have been riding for {} miles".format(self.miles)
        return self
    def reverse(self, amount =1):
        if (self.miles<=5):
            print "can not have negative miles"
        else:
            self.miles-= 5 * amount
            print "I have been riding for {} miles".format(self.miles)
            return self

print "myBike"
myBike = Bike("$200", "60")
myBike.riding(3).reverse().displayInfo()


print "basilaBike"
basilaBike = Bike("600", "100")
basilaBike.riding(2).reverse(2).displayInfo()


print "ryanBike"
ryanBike = Bike("250", "50")
ryanBike.riding().reverse().displayInfo()
