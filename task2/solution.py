def groupby(func, seq):
    storage = {}
    z = map(func, seq)
    for i in seq:
        storage.setdefault(next(z), []).append(i)
    return storage


def iterate(func):
    def identity(p):
        return p

    def composition(f1, f2):
        return (lambda x: f1(f2(x)))
    while True:
        yield identity
        identity = composition(func, identity)


def zip_with(func, *iterables):
    ziped = zip(*iterables)
    while True:
            zip_it = next(ziped)
            yield func(*zip_it)


def cache(func, cache_size):
    results = {}

    def func_cashed(x):
        if not x in results:
            results[x] = func(x)
            if (len(results) > cache_size):
                results.popitem()
        return results[x]
    return func_cashed
