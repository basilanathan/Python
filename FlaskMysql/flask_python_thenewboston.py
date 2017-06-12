from flask import flask

app = Flask(__name__) #pass it in to  help it determine the root path. websites have a bunch of pages. all of those pages will be connected to a python function. it's called routing

@app.route('/')#connect a webpage, this is the homepage of the website.
def index():#name the function watever the root is
    return 'this is the homepage' #tying a url on your website to a python function. whenever the user goes to your hompage the return is what they will see.



        #conencting a url to a return value of a function. so whenever the url the response from the server will whatever the return is.
@app.route('/tuna') #when the user goes to this page, the return statement will be the response
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):    #anytime you want to make a variable in your url, need to put in angle brackets
    return "Hey there %s" %username #if they pass in Emily it'll say hey there emily


if __name__ == "__main__" #quick check to make sure that we only run the app when the file is called directly
        app.run(debug=True) #start this webserver. website will start renning

#can make multiple webpages for your app or website using routing, tying together a url with the rturn fucntion.

FLASK HTTP METHODS

from flask import Flask, request #info about how the user requested the webpage
app = FLask(__name__)

@app.route('/')
def index():
    return "Method user: %s" % request.method #post method= for forms, or users to submit information

@app.route('/bacon', methods=['GET', 'POST']) #this bacon page is capable of handling get and post
def bacon():
    if request.method == 'POST'
        return "you are using POST"
    else:
        return "you are probably using GET"    

if __name__ == "__main__":
    app.run()
