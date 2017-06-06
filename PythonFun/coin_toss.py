head = 0
tail = 0
import random

for i in range(1,5001):
    # import random
    num= random.random()
    # print num
    num_rounded= round(num)
    # print num_rounded
    if num_rounded == 1:
        head += 1
        print "Attempt #" + str(i) + ": Throwing a coin... it's a head!... Got " + str(head) + " heads so far and " + str(tail) + " tails so far"
    if num_rounded == 0:
        tail += 1
        print "Attempt #" + str(i) + ": Throwing a coin... it's a tail!... Got " + str(head) + " heads so far and " + str(tail) + " tails so far"
    # if num_rounded == 0:
    #     tail += 1
        # print "Throwing a coin... it's a tail!... Got " + str(tail) + " tails so far"
