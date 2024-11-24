from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main():
    return "Hellow, world"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/comfi")
def comfi():
    return render_template("index.html")



app.run()