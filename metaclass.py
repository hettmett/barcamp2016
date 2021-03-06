# --- The metaclass definition, note the inheritance of type instead of object
class MetaSpam(type):

    # Notice how the __new__ method has the same arguments
    # as the type function we used earlier?
    def __new__(metaclass, name, bases, namespace):
        name = 'SpamCreatedByMeta'
        bases = (int, ) + bases
        namespace['eggs'] = 1
        return type.__new__(metaclass, name, bases, namespace)


# First, the regular Spam:
class Spam(object):
    pass


print(Spam.__name__)
print(issubclass(Spam, int))
print(Spam.eggs)


# --- Now the meta-Spam
class Spam(object, metaclass=MetaSpam):
    pass


print(Spam.__name__)
print(issubclass(Spam, int))
print(Spam.eggs)
