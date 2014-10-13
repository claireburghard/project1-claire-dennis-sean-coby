from flask import Flask, render_template, request, redirect, session
import qcheck

app=Flask(__name__)


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    message = "Butts"
    if request.method=="GET":
        return render_template("home.html", message = message)
    else:
        button = request.form['b']
        global question
        question = request.form["query"]
        if button=="Submit":
            message = qcheck.check(question)
            return render_template("home.html", message = message)

if __name__=="__main__":

    app.run()
