from operator import itemgetter


class School(object):
    def __init__(self):
        self.schoollist = {}

    def add_student(self, name, grade):
        self.schoollist[name] = grade
        return self.schoollist

    def roster(self):
        roster = []
        self.schoollist = dict(sorted(self.schoollist.items(), key=itemgetter(0)))
        for name, grade in sorted(self.schoollist.items(), key=itemgetter(1)):
            roster.append(name)
        return roster

    def grade(self, grade_number):
        graderoster = []
        for name, grade in self.schoollist.items():
            if grade == grade_number:
                graderoster.append(name)
        graderoster.sort()
        return graderoster

