def rows(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    if letter in alphabet and alphabet.index(letter) >= 1:
        lettervalue = alphabet.index(letter)
        lettercounter = 1
        width = lettervalue - 1
        result.append("{width}A{width}".format(width=" "*lettervalue))
        for i in range(lettervalue - 1):
            result.append("{width}{letter}{centerwidth}{letter}{width}".format(width=" "*width,
                                                                               letter=alphabet[lettercounter],
                                                                               centerwidth=" "*(2 * lettercounter - 1)))
            lettercounter += 1
            width -= 1
        result.append(f"{letter: <{2*lettervalue}}{letter}")
        lettercounter = 1
        width = 1
        for i in range(lettervalue - 1):
            result.append(
                "{width}{letter}{centerwidth}{letter}{width}".format(width=" "*width,
                                                                     letter=alphabet[lettervalue-lettercounter],
                                                                     centerwidth=" "*(2 * (lettervalue-lettercounter)-1)))
            lettercounter += 1
            width += 1
        result.append("{width}A{width}".format(width=" " * lettervalue))
        return result
    elif letter in alphabet and alphabet.index(letter) == 0:
        return ["A"]
    else:
        raise Exception("The diamond kana requires a single capitalized alphabetic letter as input.")
