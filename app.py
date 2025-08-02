from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
#create templates folder => index.html
def index():
    return "Welcome to our College"
@app.route("/home1")
def home1():
    return "home page"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)