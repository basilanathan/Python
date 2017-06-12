#in actual website, going to have more files, images, css, javascript, html.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index:
    retrun "<h2>Homepage</h2>" #return value of the function is the server response. so we can type HTML in here
#but never put HTML directly in FLASK

@app.route('/profile/<name>')#profile page and passing in a name
def profile(name):
    return render_template("profile.html", name=name)#what does the layout in order to know what information to display= the name variable



if __name__ == "__main__":
    app.run

<title>Welcome to thenewboston</title>
<h1>Hey there {{name}} </h1> #when you want to use a variable you want to put it in between two curly braces this gets passed through the template
#flask is generating t he html for us. uses the profil.html, throuws in the variables and returns it as a server response

{% if user %}# only going to be displayed when the user is looged in
    <h1>Hello {{user}}</h1>

{% else %}
    <h1>Please log in</h1>
{% endif %}
#content of the html is dependant of whatever variables passed im

PASSING OBJECTS INTO TEMPLATES

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/shopping")
def shopping():
    food = ["cheese", "tuna", "beef"]
    return render_template("shopping.html", food=food) #passing the variable food in. shopping template has acess to the
    # food variable which is a list

if __name__ == "__main__":
    app.run

html

<ul>
    {% for item in food %} #dont read this as html, interpret it as python and flask.
    #will loop through the list three times
        <li>{{item}}</li>
    {% endfor %}#signifies the end of the loop

</ul>
