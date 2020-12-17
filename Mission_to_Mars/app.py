from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask App
app = Flask(__name__)

# Use flask_pymongo to set up mongo connections
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Set the route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    print(mars_data)
    return render_template("index.html", mars_data=mars_data)

# Route for scrape function
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)