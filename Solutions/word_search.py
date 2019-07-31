class Point(object):
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        searches = [
            self.search_horizontally,
            self.search_horizontally_reverse,
            self.search_vertically,
            self.search_vertically_reverse,
            self.search_diagonally,
            self.search_diagonally_leftbottom,
            self.search_diagonally_rightbottom,
            self.search_diagonally_righttop
        ]
        for search in searches:
            points = search(word)
            if points:
                return points
        return None

    def search_horizontally(self, word):
        for y_index, row in enumerate(self.puzzle):
            if word in row:
                x1 = row.index(word)
                x2 = row.index(word)+len(word)
                return Point(x1, y_index), Point(x2, y_index)

    def search_horizontally_reverse(self, word):
        reversed_word = word[::-1]
        return self.search_horizontally(reversed_word)

    def search_vertically(self, word):  # more complex approach
        for y_index, row in enumerate(self.puzzle):
            start = 0
            while row.find(word[0], start) > -1:  # if the first element of the word is present:
                x = row.find(word[0], start)  # find its index position
                start = row.find(word[0], start) + 1  # new starting point of search within row (in case of multiple occurrences)
                verticalpointer = 1  # start looking vertically down, from the next row onwards
                if (y_index+verticalpointer) >= len(self.puzzle):
                    return None
                while word[verticalpointer] == (self.puzzle[y_index+verticalpointer][x]):  # see if the next letter matches up
                    verticalpointer += 1
                    if verticalpointer == len(word):
                        return Point(x, y_index), Point(x, (y_index+len(word)))

    def search_vertically_reverse(self, word):
        reversed_word = word[::-1]
        return self.search_vertically(reversed_word)

    def search_diagonally(self, word):
        for y_index, row in enumerate(self.puzzle):
            start = 0
            while row.find(word[0], start) > -1:
                x = row.find(word[0], start)
                start = row.find(word[0], start) + 1
                diagonalpointer = 1
                if (y_index+diagonalpointer) >= len(self.puzzle) or (x+diagonalpointer) >= len(row):
                    return None
                while word[diagonalpointer] == (self.puzzle[y_index+diagonalpointer][x+diagonalpointer]):
                    diagonalpointer += 1
                    if diagonalpointer == len(word):
                        return Point(x, y_index), Point(x+len(word), y_index+len(word))

    def search_diagonally_leftbottom(self, word):
        for y_index, row in enumerate(self.puzzle):
            start = 0
            while row.find(word[0], start) > -1:
                x = row.find(word[0], start)
                start = row.find(word[0], start) + 1
                diagonalpointer = 1
                if (y_index+diagonalpointer) >= len(self.puzzle) or (x+diagonalpointer) >= len(row):
                    return None
                while word[diagonalpointer] == (self.puzzle[y_index-diagonalpointer][x+diagonalpointer]):
                    diagonalpointer += 1
                    if diagonalpointer == len(word):
                        return Point(x, y_index), Point(x+len(word), y_index-len(word))

    def search_diagonally_rightbottom(self, word):
        for y_index, row in enumerate(self.puzzle):
            start = 0
            while row.find(word[0], start) > -1:
                x = row.find(word[0], start)
                start = row.find(word[0], start) + 1
                diagonalpointer = 1
                while word[diagonalpointer] == (self.puzzle[y_index-diagonalpointer][x-diagonalpointer]):
                    diagonalpointer += 1
                    if diagonalpointer == len(word):
                        return Point(x, y_index), Point(x+len(word), y_index-len(word))

    def search_diagonally_righttop(self, word):
        for y_index, row in enumerate(self.puzzle):
            start = 0
            while row.find(word[0], start) > -1:
                x = row.find(word[0], start)
                start = row.find(word[0], start) + 1
                diagonalpointer = 1
                while word[diagonalpointer] == (self.puzzle[y_index+diagonalpointer][x-diagonalpointer]):
                    diagonalpointer += 1
                    if diagonalpointer == len(word):
                        return Point(x, y_index), Point(x+len(word), y_index-len(word))