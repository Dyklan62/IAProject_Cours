import flask
import pandas as pnd
from prettytable import PrettyTable


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    dataset = pnd.read_csv("SeoulBikeData_01.csv")
    return "connected"


app.run()
