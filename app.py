from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """returns simple welcome message"""

    return "welcome"


@app.get('/welcome/home')
def welcome_home():
    """returns welcome home message"""

    return "welcome home"


@app.get('/welcome/back')
def welcome_back():
    """returns welcome back message"""

    return "welcome back"