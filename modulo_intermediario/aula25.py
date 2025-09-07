def crate_function(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return intern


def invert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma str')


invert_string_check = crate_function(invert_string)
invert = invert_string_check('123')
print(invert)
