# Find and Replace
str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
print str.replace('monkey', 'alligator')

# Min and Max
x = [2,54,-2,7,12,98]
print max(x)
print min(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]

y=[]
# y.append("hello")
# y.append("world")
y.append(x[0])
y.append(x[7])
print y

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

z= []
z.append(x.pop(0))
z.append(x.pop(0))
print x
print z

x.insert(0,z)
print x
