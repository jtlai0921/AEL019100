def highest(scores):
    return max(scores)


def lowest(scores):
    return min(scores)


def get_pass_scores(scores):
    return filter(lambda x: True if x >= 60 else False, scores)


def get_fail_scores(scores):
    return filter(lambda x: True if x < 60 else False, scores)


def average(scores):
    return sum(scores) / len(scores)