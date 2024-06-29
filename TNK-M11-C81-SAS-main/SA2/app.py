# import render_template and request from flask
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static")
app.use_static_for_root = True

# Set methods parameter as ["GET", "POST"]
@app.route("/", methods= ["GET", "POST"])
def home():
    # If request.method is "GET" the return render_template('index.html')
    if request.method == "GET":
        return render_template('index.html')
    else:    
        # Else get the sender, receiver, amount using request.form.get() method
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        
        # Print sender, receiver, amount on console
        print(sender, receiver, amount)
        
        # Return render_template('index.html)
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)