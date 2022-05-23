from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

# Set route
@app.route('/')
def home():
    scraped_data = mongo.db.scraped_data.find_one()
    return render_template("index.html", scraped_data=scraped_data)

@app.route("/scrape")
def mars_scrape():
    scraped_data = mongo.db.listings
    scraped_data_2 = scraped_data.scrape()
    scraped_data.update_one({}, {"$set": scraped_data_2}, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)