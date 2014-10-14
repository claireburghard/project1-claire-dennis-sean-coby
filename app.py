from flask import Flask, render_template, request, redirect, session
import qcheck
import text

app=Flask(__name__)

l1 = ""
l2 = ""
l3 = ""
l4 = ""
l5 = ""

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
                global l1
                global l2
                global l3
                global l4
                global l5
                if message == "who":
                    answer = text.whosearch(question)
                    a1 = answer[0]
                    a2 = answer[1]
                    a3 = answer[2]
                    a4 = answer[3]
                    a5 = answer[4]
                    links = text.linkssearch(answer)
                    print links
                    l1 = links[0]
                    print "L1: " + l1 
                    l2 = links[1]
                    l3 = links[2]
                    l4 = links[3]
                    l5 = links[4]
                elif message == "when":
                    answer = text.whensearch(question)
                    a1 = answer[0]
                    a2 = answer[1]
                    a3 = answer[2]
                    a4 = answer[3]
                    a5 = answer[4]
                    links = text.linkssearch(answer)
                    l1 = links[0]
                    print l1
                    l2 = links[1]
                    l3 = links[2]
                    l4 = links[3]
                    l5 = links[4]
                return render_template("results.html", a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)

@app.route("/a1")
def a1():
    print l1
    return redirect(l1)

@app.route("/a2")
def a2():
    return redirect(l2)

@app.route("/a3")
def a3():
    return redirect(l3)

@app.route("/a4")
def a4():
    return redirect(l4)

@app.route("/a5")
def a5():
    return redirect(l5)
    

if __name__=="__main__":
    app.debug = True
    app.run()
