# In the greet folder, Make a simple Flask app that responds to these routes with simple text messages:

# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”

from flask import Flask, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/welcome')
def say_welcome():
    return "welcome"

@app.route('/welcome/home')
def say_welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def say_welcome_back():
    return "welcome back"