
scores = [7, 3, 9, 3, 5]
scores_copy = scores.copy()
scores_copy = scores[:]
scores_copy.sort()
scores_desc = sorted(scores, reverse=True)
print(scores)  # [9, 7, 5, 3, 3]