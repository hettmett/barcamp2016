import collections

counter = collections.Counter('eggs')
for k in 'eggs':
    print('Count for %s: %d' % (k, counter[k]))


"""

import math
import collections

counter = collections.Counter()
for i in range(0, 100000):
   counter[math.sqrt(i) // 25] += 1

for key, count in counter.most_common(5):
    print('%s: %d' % (key, count))

"""
