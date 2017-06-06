# # Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number
def odd_even():
    for count in range(1, 2000):
        if count % 2 != 0:
            print "Number is " + str(count) + ". This is an odd number."
        else:
            print "Number is " + str(count) + ". This is an even number."

odd_even()
#
# # Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
# # Multiply
a = [2,4,10,16]
def multiply(a,b):
    new_list = []
    for num in a:
        new_list.append(num * b)
    print new_list
multiply(a, 5)

a = [2,4,6]
b=3
def multiple(a,b):
    for j in range(0, len(a)-1):
        ones= a[j]*b
        new_array=[]
        for i in range(0, ones):
            new_array.append(1)
        a[j]= new_array

multiple(a,b)
