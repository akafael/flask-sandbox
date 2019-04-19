from flask import Flask

# Create a Flask app with same name
app = Flask(__name__)

# Bind each page with a function using a Flask Decorator with the path
@app.route('/')
def index():
   '''Main Page'''
   return "<h1>Hello, World !</h1>"

# You can also use a custom url parammeter 
@app.route('/user/<name>')
def user(name):
   '''Custom Url Page Call'''
   return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
   app.run(debug=True)
