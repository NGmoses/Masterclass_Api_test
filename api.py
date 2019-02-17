import flask

app = flask.Flask(__name__)#creates Flask application object
app.config["DEBUG"]= True #Returns an error message when something doesn't work well

@app.route('/', methods=['GET'])#This maps the fxn 'home' to this url

def home():
    return "<h1>Distance Reading Archive<h1>"

app.run()#Methods that runs the aplication server