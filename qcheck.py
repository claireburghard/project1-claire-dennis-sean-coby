def check(question):
    qtype = question.split(' ', 1)[0]
    qtype = qtype.lower()
    if qtype == "who" or qtype == "when":
        return qtype
    else:
        return "not valid"
