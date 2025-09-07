def crate_function(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return intern


@crate_function
def invert_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma str')


invert = invert_string('123')
print(invert)
