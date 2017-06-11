from flask import Flask, render_template, redirect, request, flash
import re
from mysqlconnection import MySQLConnectior #requests the app and the database. go to your databse. make sure your on the right port.

app= Flask(__name__)
app.secret_key= "basilabasila"
mysql= MySQLConnector(app, 'emaildb') #have a way to communicate with the databse and is storing it in mysql variable

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process' methods=['POST']) #its  a post, so we need a methods post
def process():
    EMAIL_REGEX =
    re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') #^ is the begginging of the string, and the string of characters that are acceptable. + symbol refers to begin the string, you can have at least one of the characters in there. \. means literally  a period again limit to a-z $is the end of the string.
    if EMAIL_REGEX.match(request.form['email']): #lets match it to the regex
        print "this is a valid email"
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW());"
        data = {"email":request.form['email']} #go into the dictionary and find the key of email
        mynewid= mysql.query_db(query, data)
        print mynewid
        #never render on a post. you just posted data. if your render template
        flash("this is valid! Your email {} is valid!".format(request.form['email']))
        return redirect('/success')
    else:
        print "this is not a valid email"
        print 'made it here to the process route!', #you know that your submitting to where u want it to go.
        request.form['email'] #print request.form with the key of email. if you do just requet ,form itll print out a dictionary with the key value pair (email, input)
        flash('This is not a valid email')
    return redirect('/')

@app.route ('success')
def success(): #this will finish the job of rendering the template we wanted to show
    query = "SELECT * FROM emails"
    listofemails= mysql.query.db(query)
    return render_template('success.html', emails= listofemails)   #jinga knows whats on the left so emails. passing the list onto the html.

@app.route('/details/<id>') #through the url you can pass the id
def details(id):
    print "got the id", id
    query = "  SELECT * FROM emails WHERE id = {}".format(id)
    mysql.query_db(query)#nedded to pass the infor to the databse
return redirect('/')
app.run(debug=True)
