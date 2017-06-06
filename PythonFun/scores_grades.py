# import random
# num= random.random()
# print num

# for i in range(60,100):
#     import random
#     num= random.random()
#     print num

for i in range(0,10):
    import random
    score= random.randrange(60,100)
    # print score
    if 69 >= score >= 60:
        print "Score: " + str(score) + "; Your grade is D"
    elif 79 >= score >= 70:
        print "Score: " + str(score) + "; Your grade is C"
    elif 89 >= score >= 80:
        print "Score: " + str(score) + "; Your grade is B"
    elif 100 >= score >= 90:
        print "Score: " + str(score) + "; Your grade is A"
print score
print "End of the program. Bye!"
