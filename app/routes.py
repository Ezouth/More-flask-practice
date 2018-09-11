from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    name = 'Tyler'
    nameList = ['I am 26', 'My birthday is May 8']
    dictionary1 = {
    'hello' : 'there',
    'this' : 'is just for practice'
    }
    return render_template('index.html', name=name, nameList=nameList, dictionary1=dictionary1)

@app.route('/secondpage')
def second_page_func():
    person = {'name': 'Tyler',
    'height': "5'9",
    'eyes': 'blue'}
    myList = [1,2,3,4,5]
    return render_template('secondpage.html', person=person, myList=myList)

@app.route('/thirdpage')
def thirdpage_func():
    dogs = {'Pomeranian': 'Small Doggo!',
    'Corgi' : 'Small Doggo!',
    'Labrador' : 'Medium Doggo',
    'Bernese Mountain Dog' : 'HUGE DOGGO!'
    }
    dogsList = ['I', 'like', 'petting', 'dogs']
    return render_template('thirdpage.html', dogs=dogs, dogsList=dogsList )

@app.route('/redirecting')
def my_redirect():
    return redirect(url_for('index'))
