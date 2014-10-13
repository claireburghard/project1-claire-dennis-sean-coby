from flask import Flask, render_template, request, redirect, session
import qcheck
import text

app=Flask(__name__)


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    message = ""
    error_message = ""
    if request.method=="GET":
        return render_template("home.html", message = message, error_message=error_message)
    else:
        button = request.form['b']
        global question
        question = request.form["query"]
        if button=="Submit":
            message = qcheck.check(question)
            if message == "not valid":
                message = ""
                error_message = "Question must begin with who or when"
                return render_template("home.html",results = message, error_message = error_message)
            else:
                answer = ""
                if message == "who":
                    answer = text.whosearch(question)
                elif message == "when":
                    answer = text.whensearch(question)
                return render_template("home.html", results = answer, error_message = error_message)

if __name__=="__main__":
    app.debug = True
    app.run()
