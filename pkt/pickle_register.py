import sys
import cloudpickle as pickle
import inspect


def register():
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    pickle.register_pickle_by_value(sys.modules[mod.__name__])


def cloud_function(func):
    return function()(func)

    
def function(write_pk = pickle, read_pk = pickle):
    def decorator_function(func):
        data = write_pk.dumps(func)
        f = None
        def wrapper(x):
            nonlocal f, data
            if f is None:
                f = read_pk.loads(data)
                data = None
            return f(x)
        return wrapper
    return decorator_function
