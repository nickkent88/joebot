from functools import wraps

rules = {}

def handles(*keywords, **options):
    def decorator(func):
        for word in keywords:
            rules[word] = func
        return func
    return decorator


# def handles(*keywords, **options):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for word in keywords:
#                 print(keywords)
#                 rules[word] = func
#             return partial(func, *args, **kwargs)
#         return wrapper
#     return decorator

@handles('a', 'b', 'c')
def some_func(context):
    pass
                    
if __name__=='__main__':
    print(rules)
    