def raise_to_the_degrees(number, mas_degree):
    i = 0
    for _ in range(mas_degree):
        yield number**i
        i+=1

res = raise_to_the_degrees(122345, 500)
print(res)
for _ in res:
    print(_)
    print("------")
print("new")
for _ in res:
    print(_)
    print("------")