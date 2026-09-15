def passed(score):
    return score >= 40

assert passed(40)
assert passed(75)
assert not passed(39)
