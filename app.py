from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template("home.html", **{"site": None, "search": None})

@app.route('/list', methods=['GET'])
def list():
    # List s3 bucket contents
    raise NotImplementedError

@app.route('/create', methods=['POST'])
def create():
    # generate config that will load a specific site and search query 
        '''
            {
                "site": "en.wikipedia.org/wiki/Dog",
                "search": "Beagles are cool"
            }
        '''
    # generate hash based on content of config
    # store config underneath hash key in s3

    return render_template("home.html")
