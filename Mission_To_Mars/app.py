from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Set route
@app.route('/')
def home():
    return render_template('index.html', )

@app.route('/scrape')
def scrape():
    return render_template('index.html', )

if __name__ == "__main__":
    app.run(debug=True)