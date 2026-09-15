def percentage(score, total):
    return score * 100 / total if total else 0

assert percentage(50, 100) == 50
assert percentage(0, 100) == 0
