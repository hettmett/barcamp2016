import abc


class Spam(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def some_method(self):
        raise NotImplemented()


class Eggs(Spam):

    def some_new_method(self):
        pass


eggs = Eggs()


class Bacon(Spam):
    def some_method():
        pass


bacon = Bacon()
