def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u",
                "v", "w", "x", "y", "z"]
    for letter in alphabet:
        if letter in sentence:
            continue
        else:
            return False
    return True