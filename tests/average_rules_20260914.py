def average(values):
    return sum(values) / len(values) if values else 0

assert average([100, 100]) == 100
assert average([60, 80]) == 70
assert average([]) == 0
print('Grade average rules passed')
