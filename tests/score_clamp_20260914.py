def safe_score(value):
    return max(0, min(100, value))

assert safe_score(50) == 50
assert safe_score(-5) == 0
assert safe_score(105) == 100
print('Score clamp rules passed')
