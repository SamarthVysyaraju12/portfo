from flask import Flask, render_template

app = Flask(__name__)


# sending html files through routes, so when you enter these routes the HTML files show on screen
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
