class Registry(object):

    __slots__ = ('attrs', 'items')

    def __init__(self):
        self.items = {}
        super().__init__()

    def __setitem__(self, key, val):
        self.items[key] = val

    def __getitem__(self, key):
        return self.items.get(key)

    '''def get_count(self):
        return len(self.items)

    def set_count(self, val):
        raise Exception('Can not set count of registry items')

    count = property(get_count, set_count)'''

    @property
    def count(self):
        return len(self.items)

    @count.setter
    def count(self, val):
        raise Exception('Can not set count of registry items')


inst = Registry()

inst['name'] = 'John'
print(inst['name'])

print(inst.count)
inst.count = 10
