def checker(var_1):
    if type(var_1) != str: # ! =
        raise TypeError(f"Sorry, we canot work with {type(var_1)}", f"we need class str")
    else:
        return var_1

first_var = 10
checker(first_var)