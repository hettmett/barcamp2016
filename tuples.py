import pprint


# flat tuples
spam = 1, 2, 3
eggs = 4, 5, 6

data = dict()
data[spam] = 'spam'
data[eggs] = 'eggs'

pprint.pprint(data)


# very complex tuple
spam = 1, 'abc', (2, 3, (4, 5)), 'def'
eggs = 4, (spam, 5), 6

data = dict()
data[spam] = 'spam'
data[eggs] = 'eggs'

pprint.pprint(data)

# -- extended unpacking
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)
