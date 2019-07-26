def is_valid(isbn):
    isbn_hyphenless = list("".join(isbn.split("-")))
    if len(isbn_hyphenless) != 10:
        return False
    isbn_x = [10 if i == "X" else i for i in isbn_hyphenless]
    for i in isbn_x:
        if not i == 10 and not i.isdigit():
            return False
    if 10 in isbn_x[:-1]:
        return False
    return (int(isbn_x[0]) * 10 + int(isbn_x[1]) * 9 + int(isbn_x[2]) * 8 + int(isbn_x[3]) * 7 + int(isbn_x[4]) * 6 +
            int(isbn_x[5]) * 5 + int(isbn_x[6]) * 4 + int(isbn_x[7]) * 3 + int(isbn_x[8]) * 2 + int(isbn_x[9])) % 11 == 0

