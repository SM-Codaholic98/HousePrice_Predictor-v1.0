from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("D:\\Predictor_Applications v1.2\\HousePrice_Predictor v1.2\\HousePrice.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        income = float(request.form['Avg. Area Income'])
        house_age = float(request.form['Avg. Area House Age'])
        no_of_rooms = float(request.form['Avg. Area Number of Rooms'])
        no_of_bedrooms = float(request.form['Avg. Area Number of Bedrooms'])
        population = float(request.form['Area Population'])
        
        prediction = model.predict([[income, house_age, no_of_rooms, no_of_bedrooms, population]])
        output=round(prediction[0],2)

        return render_template('WebApp.html',prediction_text="Your House price is ${}".format(output))

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(debug=True)