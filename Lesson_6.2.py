try:
    print("Start code")
    print(10/0)
    print("No error")
except (ZeroDivisionError, NameError):
    print("We have an zero division or name error")


print("Code after capsule")