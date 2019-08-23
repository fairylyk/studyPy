import functools


def a_new_decorator(a_func):

    @functools.wraps(a_func)
    def wrapper(*args, **kw):
        print 'call %s():' % a_func.__name__

        a_func(*args, **kw)

        print 'end %s():' % a_func.__name__

    return wrapper

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
# Output: a_function_requiring_decoration