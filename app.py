from flask import Flask, request, render_template, redirect,session

app=Flask(__name__)


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("home.html")

if __name__=="__main__":

    app.run()
