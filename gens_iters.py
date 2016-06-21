import itertools


def sequence(n):
    for i in range(n):
        yield i


print(sequence(5))
print(next(sequence(5)))

print('\n> Iteration result')
for i in sequence(5):
    print(i)


# repeat number of times
print(list(itertools.repeat('ABC', 3)))

# cartesian product
# print(list(itertools.product('ABC', '123')))

# permutations
# print(list(itertools.permutations('ABC')))
# print(list(itertools.permutations('ABC', 2)))

# combinations
# print(list(itertools.combinations('ABC', 2)))
