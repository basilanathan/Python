# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# for d in students:
#     x= d['first_name']
#     y= d['last_name']
#     print x + " " + y

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def Names_1(key, title):
	print title
	for x in range(len(key)):
		full_name = key[x]['first_name'] + " " + key[x]['last_name']
		print (x + 1), "-", full_name, "-", (len(full_name) - 1)

students = users['Students']
instructors = users['Instructors']

Names_1(students, 'Students')
Names_1(instructors, 'Instructors')
