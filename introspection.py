# def introspection_info(obj):
#     type_ = type(obj)
#     attr_ = vars(obj)
#
#     return  (type_,attr_)
#
# g = 1
# print(introspection_info(g))
import inspect
import types


def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = dir(obj)
    info['attributes'] = [attr for attr in attributes if not attr.startswith('__')]

    methods = [method for method in attributes if callable(getattr(obj, method)) and not method.startswith('__')]
    info['methods'] = methods

    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

    info['docstring'] = inspect.getdoc(obj)
    info['is_callable'] = callable(obj)

    return info
