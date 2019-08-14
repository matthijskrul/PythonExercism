import itertools
from re import findall


def solve(puzzle):
    words = findall("[A-Z]+", puzzle)
    firstletters = {word[0] for word in words}
    n = len(firstletters)

    letters = findall("[A-Z]", puzzle)
    uniquechars_unordered = set()
    uniquechars_ordered = []  # necessary because output should be dict of letters and numbers, not solution!
    for letter in letters:
        if letter not in uniquechars_unordered:
            uniquechars_unordered.add(letter)
            uniquechars_ordered.append(letter)

    sortedchars = "".join(firstletters) + "".join(uniquechars_unordered - firstletters)

    encoded_digits = tuple(ord(c) for c in "0123456789")
    encoded_characters = tuple(ord(c) for c in sortedchars)
    zero = encoded_digits[0]
    for i in itertools.permutations(encoded_digits, len(encoded_characters)):
        if zero not in i[:n]:  # numbers may not begin with zero
            solution = puzzle.translate(dict(zip(encoded_characters, i)))
            if eval(solution):
                numbers = ("".join(uniquechars_ordered)).translate(dict(zip(encoded_characters, i)))
                # create a string of the correct numbers corresponding to the unique characters
                numbers = list(map(int, numbers))  # convert string to list of ints
                stringchars = list(uniquechars_ordered)
                resultzip = zip(stringchars, numbers)  # create correspondence between numbers and letters
                return dict(resultzip)
