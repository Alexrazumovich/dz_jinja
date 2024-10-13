from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    context={
        'title': 'Home Page',
        'content': 'This is the home page content.'
    }
    return render_template('home.html',**context)


@app.route('/about')
def about():
    context={
        'title': 'About Page',
        'content': 'This is the about page content.'
    }
    return render_template('about.html',**context)
