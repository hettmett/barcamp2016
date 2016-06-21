nodes = [
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'a'),
    ('b', 'd'),
    ('c', 'a'),
    ('d', 'a'),
    ('d', 'b'),
    ('d', 'c'),
]


graph = dict()
for from_, to in nodes:
    if from_ not in graph:
        graph[from_] = []
    graph[from_].append(to)


import collections

graph = collections.defaultdict(list)
for from_, to in nodes:
    graph[from_].append(to)


import json
import collections


def tree(): return collections.defaultdict(tree)


colours = tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000
colours['primary']['green'] = 0x00FF00
colours['primary']['blue'] = 0x0000FF
colours['secondary']['yellow'] = 0xFFFF00
colours['secondary']['aqua'] = 0x00FFFF
colours['secondary']['fuchsia'] = 0xFF00FF

print(json.dumps(colours, sort_keys=True, indent=4))
