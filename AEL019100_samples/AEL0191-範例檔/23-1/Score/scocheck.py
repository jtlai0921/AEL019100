# 找出最高分
def highest(scores):
    return max(scores)

# 找出最低分
def lowest(scores):
    return min(scores)

# 找出所有及格的分數
def get_pass_scores(scores):
    return filter(lambda x: True if x >= 60 else False, scores)

# 找出所有不及格的分數
def get_fail_scores(scores):
    return filter(lambda x: True if x < 60 else False, scores)

# 計算平均分數
def average(scores):
    return sum(scores) / len(scores)
