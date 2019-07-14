class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")

    def row(self, index):
        rowlist = []
        for i in self.rows[index-1].split(" "):
            rowlist.append(int(i))
        return rowlist

    def column(self, index):
        columnlist = []
        for i in range(len(self.rows)):
            columnlist.append(int(self.rows[i].split(" ")[index-1]))
        return columnlist
