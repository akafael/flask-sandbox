from flask import Flask, render_template, url_for

app = Flask(__name__)

# Man Page
@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')

# Using Url Params sample for a custom user title and Jinja templates
# it will replace all {{name}} inside user.html with the url defined name
@app.route('/user/<name>')
def user(name):
   return render_template('user.html',name=name)

# Add a Custom Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
   app.run(debug=True)
