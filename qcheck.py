def check(question):
    qtype = question.split(' ', 1)[0]
    if qtype == "Who" or qtype == "who":
        return "who"
    if qtype == "When" or qtype == "when":
        return "when"
    else:
        return "not valid"
