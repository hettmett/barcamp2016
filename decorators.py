import functools


def mk_double(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return decorated


def times(val):
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            return val * func(*args, **kwargs)
        return decorated
    return decorator


@mk_double
def plus(a, b):
    return a + b


@times(2)
def power(a, b):
    return a ** b


print(plus(1, 2))
print(power(3, 2))
