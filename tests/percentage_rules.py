def percentage(scored, total):
    return (scored / total) * 100 if total else 0

assert percentage(50, 100) == 50
assert percentage(0, 100) == 0
assert percentage(25, 50) == 50
assert percentage(10, 0) == 0
print('Percentage rules passed')
