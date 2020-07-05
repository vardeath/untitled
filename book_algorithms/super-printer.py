from functools import wraps


def printer(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache.keys():
            text = 'from cache: ' + cache[args]
        else:
            values = [str(a) for a in args]
            text = ', '.join(values)
            text += ' | '
            text += str(func(*args))
            cache[args] = text
        name = func.__name__
        print('{} - {} operation'.format(text, name))

    return wrapper


@printer
def multiplier(*args):
    result = 1
    for value in args:
        result *= value
    return result


@printer
def addition(*args):
    result = 0
    for value in args:
        result += value
    return result


@printer
def exponentiation(*args) -> str:
    '''Discription'''
    result = 2
    for value in args:
        result **= value
    return result


addition(2, 4, 4)
multiplier(2, 4, 4)
addition(2, 4, 4)
multiplier(2, 4, 4)
exponentiation(2, 2, 1)
exponentiation(2, 2, 1)
print(exponentiation.__name__)
print(exponentiation.__annotations__)
