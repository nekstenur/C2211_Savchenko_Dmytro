import random
import sys
import requests
import inspect

otstup = f"{'':-^50}"
print(otstup)

print(inspect.ismodule(random))
print(inspect.isclass(random))
print(inspect.isfunction(random))

print(otstup)

print(inspect.getmodule(random))
print(inspect.getmodule(list))

print(otstup)

print(random.getstate)
print(random.getrandbits)

print(otstup) #das

for module_name, module_path in sys.modules.items():
    name_of_module = f"{module_name:^50}"
    print(name_of_module, module_path)

print(otstup)