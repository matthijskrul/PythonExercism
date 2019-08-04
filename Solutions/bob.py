def response(hey_bob):
    hey_bob = hey_bob.replace(" ", "")
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?" and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob[-1] == "?":
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
