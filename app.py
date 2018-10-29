from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template("home.html")
