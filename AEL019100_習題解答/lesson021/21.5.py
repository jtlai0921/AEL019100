def check_scores(scores):
    for i in range(len(scores)):
        if 55 <= scores[i] < 60:
            scores[i] = 60

scores = [90, 75, 55, 80, 57, 60]

check_scores(scores)

print(scores)
