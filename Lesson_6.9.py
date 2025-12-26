def checker(var_1):
    if not var_1 % 5 == 0: # ! =
        raise TypeError(f"{var_1}, не ділиться на 5 без остачи! Буде {var_1 / 5}!")
    else:
        return var_1


first_var = 15
second_var = 101
trete_var = 14

checker(first_var)
checker(second_var)
checker(trete_var)