import collections


spam = collections.OrderedDict()
spam['b'] = 2
spam['c'] = 3
spam['a'] = 1
print(spam)

print(collections.OrderedDict([('b', 2), ('c', 3), ('a', 1)]))

for key, value in spam.items():
    print(key, value)

eggs = collections.OrderedDict(sorted(spam.items()))
print(eggs)
