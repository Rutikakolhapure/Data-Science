from flask import Flask, render_template
from flask import request
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application  # for compatibility with some deployment setups

# import ridge regression model and scaler

ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
Standard_scaler = pickle.load(open("models/scaler.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        return render_template("home.html")
    return render_template("home.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0")