class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self, amount=1):
        self.health -= 1 * amount
        return self

    def run(self, amount =1):
        self.health -= 5 * amount
        return self

    def displayHealth(self):
        print "Animal: {}, Health: {}".format(self.name, self.health)

animal= Animal("Lion")
animal.walk(3).run(2).displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(self)
        self.health += 50
        self.name = name

    def pet(self, amount = 1):
        self.health += 5 * amount
        return self

sakila= Dog("Dog")
sakila.walk(3).run(2).pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(self)
        self.health += 70
        self.name = name

    def fly(self, amount = 1):
        self.health -= 10 * amount
        return self

    def displayHealth(self):
        print "This is a Dragon!!"
        super(Dragon, self).displayHealth()
        return self

drogon = Dragon("Drogon")
drogon.walk(3).run(2).fly(2).displayHealth()
