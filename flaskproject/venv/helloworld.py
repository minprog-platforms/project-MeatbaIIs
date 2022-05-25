from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Index Page'

#from markupsafe import escape

@app.route("/<name>")
def hello():
    return f"Hello, world!"

