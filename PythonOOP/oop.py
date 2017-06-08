# Object oriented programming
#
# Objects have properties (attributes) and methods
# var arr=[1,2,3,4,5]
# an array has methods (.pop(), .push()) and attributes (.len())
#
# class cat
# (attributes)
#   tail
#   whiskers
#   breed
#   color
#   size
#   name
# (methods)
#   meow
#   jump
#   murder
#   cuddle
#   scratch purr
#   poop
#
# #making a class
# class Cat(object): #making a class of cat and it is an object
#   def __init__(self, name, color, breed): #when you make an instance of cat we will run this method.
#       self.name = name
#       self.color = color
#       self.breed = breed
#
# #making an instance
# kevin= Cat("Kevin", "grey", "stray") #just made Kevin
# qBert= Cat("QBert", "white", "tiger")
# kevin.murder("lizard")
#
# def murder(self, animal):
#     print "Youkilled {}" .formal(animal)

# class Card(object):
#
#     suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
#               "8", "9", "10", "Jack", "Queen", "King"]
#
#     def __init__(self, suit=0, rank=2):
#         self.suit = suit
#         self.rank = rank
#
# class Deck(object):
#     def __init__(self):
#         self.cards = []
#         for suit in range(4):
#             for rank in range(1, 14):
#                 card = Card(suit, rank)
#                 self.cards.append(card)

# def define_cards(n):
#     rank_string = ("ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
#     suit_string = ("clubs","diamonds","hearts","spades")
#     cards = []
#     for suit in range(4):
#         for rank in range(13):
#             card_string = rank_string[rank] + " of " + suit_string[suit]
#             cards.append(card_string)
#
# print "The cards are:"
# for i in range(52):              #how to make this for loop work??
#     print i

class Deck(object):
    def __init__ (self)

        rank_string = ("ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
        suit_string = ("clubs","diamonds","hearts","spades")
        cards = []

        for suit in suit_string:
            for rank in rank_string:
                cards.append(card(suit,rank))
                # print '%s %s of %s' % (n,rank,suit)
                # cards.append('%s %s of %s' % (n,rank,suit))
                n+=1
                # print cards


define_cards()
