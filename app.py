import joblib
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
model = joblib.load("regression")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form['rates'])
        model = joblib.load("regression")
        result = model.predict([[rates]])
        return(render_template("index.html", result=result[0][0]))
    else:
        return(render_template("index.html", result="NOTSUPPORT"))


if __name__ == "__main__":
    app.run()
