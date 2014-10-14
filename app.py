from flask import Flask, render_template, request, redirect, session
import qcheck
import text

app=Flask(__name__)


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    error_message = ""
    if request.method=="GET":
        return render_template("home.html", error_message=error_message)
    else:
        button = request.form['b']
        global question
        question = request.form["query"]
        if button=="Submit":
            message = qcheck.check(question)
            if message == "not valid":
                message = ""
                error_message = "Question must begin with who or when"
                return render_template("home.html", error_message = error_message)
            else:
                answer = ""
                if message == "who":
                    answer = text.whosearch(question)
                    a1 = answer[1]
                    a2 = answer[2]
                    a3 = answer[3]
                    a4 = answer[4]
                    a5 = answer[5]
                    links = text.linkssearch(answer)
                    l1 = links[1]
                    l2 = links[2]
                    l3 = links[3]
                    l4 = links[4]
                    l5 = links[5]
                elif message == "when":
                    answer = text.whensearch(question)
                    a1 = answer[1]
                    a2 = answer[2]
                    a3 = answer[3]
                    a4 = answer[4]
                    a5 = answer[5]
                    links = text.linksearch(answer)
                    l1 = links[1]
                    l2 = links[2]
                    l3 = links[3]
                    l4 = links[4]
                    l5 = links[5]
                return render_template("results.html", a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, l1 = l1, l2 = l2, l3 = l3, l4 = l4, l5 = l5)

@app.route("/a1")
def a1():

if __name__=="__main__":
    app.debug = True
    app.run()
