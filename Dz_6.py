result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Значення мають бути числами")
    if a < b:
        raise ValueError("Число a менше за b")
    if b > 100:
        raise IndexError("Число b занадто велике")

    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8 : 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as exp:
        print("Помилка:", exp)

print("\nФінальний список результатів:", result)