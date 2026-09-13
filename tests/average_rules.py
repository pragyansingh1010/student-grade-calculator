def average(values):
    return sum(values) / len(values) if values else 0

assert average([]) == 0
assert average([80, 90, 100]) == 90
assert average([50]) == 50
print('Grade average rules passed')
