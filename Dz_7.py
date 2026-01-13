class iter_class:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        for item in self.data:
            yield f"Элемент: {item}"

my_obj = iter_class([1, 2, 3])

it = iter(my_obj)

print(type(it))
print(next(it))