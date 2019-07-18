class Clock(object):
    def __init__(self, hour, minute):
        self.hours = hour
        self.minutes = minute

    def to_minutes(self):
        return self.hours * 60 + self.minutes

    def __repr__(self):
        return "{:02d}:{:02d}".format(((self.hours * 60 + self.minutes) // 60) % 24,
                                      (self.hours * 60 + self.minutes) % 60)

    def __eq__(self, other):
        return self.to_minutes() % 1440 == other.to_minutes() % 1440

    def __add__(self, minutes):
        return Clock((self.to_minutes() + minutes) // 60, (self.to_minutes() + minutes) % 60)

    def __sub__(self, minutes):
        return Clock((self.to_minutes() - minutes) // 60, (self.to_minutes() - minutes) % 60)
