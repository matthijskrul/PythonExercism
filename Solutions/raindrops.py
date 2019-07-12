def convert(number):
    basestring = ""
    if number % 3 == 0:
        basestring += "Pling"
        if number % 5 == 0:
            basestring += "Plang"
            if number % 7 == 0:
                basestring += "Plong"
        elif number % 7 == 0:
            basestring += "Plong"
    elif number % 5 == 0:
        basestring += "Plang"
        if number % 7 == 0:
            basestring += "Plong"
    elif number % 7 == 0:
        basestring += "Plong"
    else:
        return str(number)
    return basestring
