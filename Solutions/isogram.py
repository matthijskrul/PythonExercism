import re


def is_isogram(string):
    lowerstring = string.lower()
    alphabet = re.compile("[a-z]")
    for char in lowerstring:
        if alphabet.search(char) and len(re.findall(char, lowerstring)) > 1:
            return False
    else:
        return True
