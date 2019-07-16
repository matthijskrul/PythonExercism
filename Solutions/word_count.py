import re


def count_words(sentence):
    regexsentence = re.split("[^a-zA-Z0-9']+", sentence)
    wordlist = {}
    for word in regexsentence:
        if word == '':
            continue
        else:
            word = word.lower()
            word = word.strip("\'")
            wordlist[word] = wordlist.get(word, 0) + 1
    return wordlist
