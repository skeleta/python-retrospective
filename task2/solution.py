from collections import OrderedDict


def groupby(func, seq):
    storage = {}
    key = map(func, seq)
    for item in seq:
        storage.setdefault(next(key), []).append(item)
    return storage


def iterate(func):
    identity = lambda arguments: arguments

    def composition(first_function, second_function):
        return (lambda arg: first_function(second_function(arg)))
    while True:
        yield identity
        identity = composition(func, identity)


def zip_with(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def cache(func, cache_size):
    cached_args = OrderedDict()

    if cache_size <= 0:
        return func

    def func_cashed(*args):
        if args not in cached_args:
            if (len(cached_args) >= cache_size):
                cached_args.popitem(False)
            cached_args[args] = func(*args)
        return cached_args[args]
    return func_cashed
