class Spam(object):

    def get_eggs(self):
        print('getting eggs')
        return self._eggs

    def set_eggs(self, eggs):
        print('setting eggs to %s' % eggs)
        self._eggs = eggs

    def delete_eggs(self):
        print('deleting eggs')
        del self._eggs

    eggs = property(get_eggs, set_eggs, delete_eggs)

    @property
    def spam(self):
        print('getting spam')
        return self._spam

    @spam.setter
    def spam(self, spam):
        print('setting spam to %s' % spam)
        self._spam = spam

    @spam.deleter
    def spam(self):
        print('deleting spam')
        del self._spam


spam = Spam()
spam.eggs = 123

spam.eggs

del spam.eggs
