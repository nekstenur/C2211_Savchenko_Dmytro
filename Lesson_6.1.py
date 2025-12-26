try:
    print("Start code")
    print(10/0)
    print("No error")
except ZeroDivisionError:
    print("We have an zero division error")
except NameError:
    print("We have an name error")

print("Code after capsule")