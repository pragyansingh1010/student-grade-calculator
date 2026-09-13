def grade(mark):
    if mark >= 90: return 'A+'
    if mark >= 80: return 'A'
    if mark >= 70: return 'B'
    if mark >= 60: return 'C'
    if mark >= 50: return 'D'
    return 'F'

assert grade(100) == 'A+'
assert grade(90) == 'A+'
assert grade(50) == 'D'
assert grade(49) == 'F'
print("Grade calculator boundary tests passed")
