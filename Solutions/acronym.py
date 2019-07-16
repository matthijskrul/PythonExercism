import re


def abbreviate(words):
    acronym = ""
    regexwords = re.split("[^a-zA-Z0-9']", words)
    for word in regexwords:
        if word == '':
            continue
        else:
            acronym += word[0].upper()
    return acronym
