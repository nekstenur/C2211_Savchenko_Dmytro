import colorama
import sys
import inspect

otstup = f"{'':-^50}"
print(otstup)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))

print(otstup)

print(inspect.getmodule(colorama))
print(inspect.getmodule(list))

print(otstup)

for module_name, module_path in sys.modules.items():
    name_of_module = f"{module_name:^50}"
    print(name_of_module, module_path)

print(otstup)