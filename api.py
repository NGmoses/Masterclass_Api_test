import flask
from flask import request, jsonify

app = flask.Flask(__name__)#creates Flask application object
app.config["DEBUG"] = True #Returns an error message when something doesn't work well

#Create some test data for our catalog in the form of a list of dictionaries.
books = [
        {
                "id": 0,
                "title": "A fire upon the deep",
                "author": "Vernor vinge",
                "first_sentence": "The cold sleep itself was dreamless.",
                "year_published": "1992",}
        {
                "id": 1,
                "title": "The one who walks away",
                "author": "Nsubuga Moses",
                "first_sentence": "The hot sleep itself was dreamless.",
                "year_published": "1993"
        }
        {
                "id": 2,
                "title": "A fire upon the deepshallow",
                "author": "Vernor Moses",
                "first_sentence": "Cold sleep itself was dreamless.",
                "year_published": "1994"
        }
]

@app.route('/', methods=['GET'])#This maps the fxn 'home' to this url

def home():
    return '''<h1>Distance Reading Archive<h1>
    <p>A prototype API for distant reading of fiction novels.</p>'''

#A route to return all of the available entries in our catalog

@app.route('api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()#Methods that runs the aplication server