from functools import wraps

# Decorators
def swap(func):
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        new_string = orig_val.swapcase()
        return new_string
    return wrapper

def sure(func):
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)

        def capitalize_every_other(string):
            result = ""
            prev_char_cap = False #we want first letter to be capitalized
            for char in string:
                if prev_char_cap: 
                    result = result + char.lower()
                else:
                    result = result + char.upper()
                prev_char_cap = not prev_char_cap
            return result

        new_string = capitalize_every_other(orig_val)
        return new_string
    return wrapper


# Iterators


@swap
def say(txt):
    return txt

@sure
def yes(txt):
    return txt

if __name__ == "__main__":
    print(say('I think not'))
    print(yes('Great Idea'))
