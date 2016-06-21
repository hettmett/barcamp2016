import pprint


class Spam(object):
    def some_instancemethod(self, *args, **kwargs):
        print('self: %r' % self)
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % pprint.pformat(kwargs))

    @classmethod
    def some_classmethod(cls, *args, **kwargs):
        print('cls: %r' % cls)
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % pprint.pformat(kwargs))

    @staticmethod
    def some_staticmethod(*args, **kwargs):
        print('args: %s' % pprint.pformat(args))
        print('kwargs: %s' % pprint.pformat(kwargs))

# Create an instance so we can compare the difference between
# executions with and without instances easily
spam = Spam()

# With an instance (note the lowercase spam)
spam.some_instancemethod(1, 2, a=3, b=4)

# Without an instance (note the capitalized Spam)
Spam.some_instancemethod()

# But what if we add parameters? Be very careful with these!
# Our first argument is now used as an argument, this can give
# very strange and unexpected errors
Spam.some_instancemethod(1, 2, a=3, b=4)

# Classmethods are expectedly identical
spam.some_classmethod(1, 2, a=3, b=4)

Spam.some_classmethod()

Spam.some_classmethod(1, 2, a=3, b=4)

# Staticmethods are also identical
spam.some_staticmethod(1, 2, a=3, b=4)

Spam.some_staticmethod()

Spam.some_staticmethod(1, 2, a=3, b=4)
