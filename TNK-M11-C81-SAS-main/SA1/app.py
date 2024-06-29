# Import flask framework
from flask import Flask

# Createa a new flask app
app = Flask(__name__)

# Create a route "/"
@app.route("/")

# Define home() trigger function taht returns a string "Welcome to Block Jinja"
def home():   
    return "Welcome to Block Jinja"

# Check if __name___ == '__main__' and run the app i.e server
if __name__ == '__main__':
    app.run(debug=True)