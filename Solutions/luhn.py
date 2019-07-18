import re


class Luhn(object):
    def __init__(self, card_num):
        self.number = card_num

    def valid(self):
        if re.search("[^0-9 ]", self.number) or len(re.findall("[0-9]", self.number)) <= 1:
            return False
        else:
            digits = re.sub("[^0-9]", "", self.number)
            digits = list(map(int, digits))
            i = len(digits)-2
            while i >= 0:
                digits[i] = digits[i] * 2
                if digits[i] > 9:
                    digits[i] = digits[i] - 9
                i -= 2
            return sum(digits) % 10 == 0
