import random
import sys
import requests

for module_name, module_path in sys.modules.items():
    name_of_module = f"{module_name:^50}"
    print(name_of_module, module_path)