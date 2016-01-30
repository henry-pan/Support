from flask import request, redirect
import web
from flask import Flask
app = Flask(__name__)

app = web.application(globals())

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/signup', methods = ['POST'])
def signup():
    print("HERE!")
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8020)
    
