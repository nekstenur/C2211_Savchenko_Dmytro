import requests
import inspect

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))
