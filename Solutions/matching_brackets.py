def is_paired(input_string):
    openbrackets = ("(", "{", "[")
    closebrackets = (")", "}", "]")
    bracketorder = []
    for char in input_string:
        if char in openbrackets:
            bracketorder.append(char)
        elif char in closebrackets:
            idx = closebrackets.index(char)
            if len(bracketorder) == 0 or bracketorder[-1] != openbrackets[idx]:
                return False
            else:
                bracketorder.pop()
    return len(bracketorder) == 0
