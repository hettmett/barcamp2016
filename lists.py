primes = set((1, 2, 3, 5, 7))

# Classic solution
items = list(range(10))
for prime in primes:
    items.remove(prime)

print(items)

# List comprehension
items = list(range(10))
items = [item for item in items if item not in primes]
print(items)

# Filter
items = list(range(10))
items = list(filter(lambda item: item not in primes, items))
print(items)
