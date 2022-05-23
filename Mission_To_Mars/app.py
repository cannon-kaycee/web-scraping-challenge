from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)

# Set route
@app.route('/')
def home():
    listings = mongo.db.listings.find_one()
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def mars_scrape():
    listings = mongo.db.listings
    listings_data = scraped_data.scrape()
    listings.update_one({}, {"$set": listings_data}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)