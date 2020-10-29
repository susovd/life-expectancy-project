# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about_us.html")
def about_us():
    return render_template("about_us.html")

@app.route("/visualisations.html")
def visualisations():
    return render_template("visualisations.html")   


if __name__ == "__main__":
    app.run(debug=True)