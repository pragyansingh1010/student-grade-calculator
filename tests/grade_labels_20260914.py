def grade(score):
    if score >= 90: return 'A+'
    if score >= 80: return 'A'
    if score >= 70: return 'B'
    if score >= 60: return 'C'
    if score >= 50: return 'D'
    return 'F'

assert grade(95) == 'A+'
assert grade(85) == 'A'
assert grade(75) == 'B'
assert grade(65) == 'C'
assert grade(55) == 'D'
assert grade(45) == 'F'
print('Grade labels passed')
