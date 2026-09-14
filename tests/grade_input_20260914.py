def valid_mark(x):
    return isinstance(x, (int, float)) and 0 <= x <= 100

assert valid_mark(0)
assert valid_mark(100)
assert valid_mark(75.5)
assert not valid_mark(-1)
assert not valid_mark(101)
print('Grade input validation passed')
