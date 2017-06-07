x= [4,6,1,3,5,7,25]
def draw_stars():

    for i in range(0, len(x)):
        strings = " "
        # print x[i]
        for j in range(0, x[i]):
            strings += '*'
        print strings
draw_stars()

# partII

x= [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def draw_stars():

    for items in x:
        strings = " "
        if type(items) == int:
            for j in range(items):
                strings += '*'
            print strings
        else:

            for num in range(0, len(items)):
                strings += items[0]
            print strings.lower()

draw_stars()
