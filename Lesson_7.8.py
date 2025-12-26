def checker(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
    except Exception as exc:
        print(f"We had a problem: {exc}")
    else:
        print(f"No problem. Result - {result}")
    return checker


def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate(2+2)