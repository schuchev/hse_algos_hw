import functools

def tracer(func):
    depth = 0 
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        t = "  " * depth 
        print(f"{t} {func.__name__}{args}{f', {kwargs}' if kwargs else ''}")


        depth += 1
        result = func(*args, **kwargs)
        depth -= 1

        print(f"{t} {func.__name__}{args}{f', {kwargs}' if kwargs else ''} = {result}")
        return result

    return wrapper

