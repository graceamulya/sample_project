from flask import Flask
app=Flask(_name_)
@app.route("/")
def index():
    return "Welcome to our College"
if _name=="main_":
    app.run(host='0.0.0.0',port=10000)