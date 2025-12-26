def checker(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"We had a problem: {exc}")
    else:
        print(f"No problem. Result - {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)

calculate(2+2)