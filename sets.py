a = set('spam')
print(sorted(a))

b = set('eggs')
print(sorted(b))

print(a & b)  # Every item in both
print(a | b)  # Every item in either or both
print(a ^ b)  # Every item in either not in both
print(a - b)  # Every item in the first bu not the latter
print(b - a)  # Every item in the first bu not the latter
print(a > b)  # True if every item in the latter is in the first
print(b > a)  # True if every item in the latter is in the first
print(a > set('sp'))  # True if every item in the latter is in the first
print(a < set('sp'))  # True if every item in the first is contained in the latter
