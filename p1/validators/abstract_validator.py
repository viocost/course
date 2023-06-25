def validator(description):
    def decorator(function):
        def wrapper():
            if function():
                print(f"pass,{description}")
            else:
                print(f"fail,{description}")
        return wrapper
    return decorator
