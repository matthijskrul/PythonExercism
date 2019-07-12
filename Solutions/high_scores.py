def latest(scores):
    if not isinstance(scores, list):
        raise Exception("Argument is not a set of scores in list format")
    return scores[len(scores)-1]


def personal_best(scores):
    if not isinstance(scores, list):
        raise Exception("Argument is not a set of scores in list format")
    return max(scores)


def personal_top_three(scores):
    toplist = []
    if not isinstance(scores, list):
        raise Exception("Argument is not a set of scores in list format")
    elif len(scores) <= 3:
        for i in range(len(scores)):
            toplist.append(max(scores))
            scores.remove(max(scores))
    else:
        for i in range(3):
            toplist.append(max(scores))
            scores.remove(max(scores))
    return toplist