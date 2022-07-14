from  flask import Flask

app = Flask(__name__)


@app.route("/")
def index ():
    return "wwwwwwwwww"


app.run(host='localhost', port=5000)