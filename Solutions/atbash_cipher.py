import string


def encode(plain_text):
    encoding = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    plain_text = plain_text.lower()
    plain_text = plain_text.translate(plain_text.maketrans("", "", string.punctuation))
    plain_text = plain_text.replace(" ", "")
    encoded_text = plain_text.translate(encoding)
    return " ".join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text):
    decoding = str.maketrans("zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz")
    ciphered_text = ciphered_text.replace(" ", "")
    return ciphered_text.translate(decoding)
