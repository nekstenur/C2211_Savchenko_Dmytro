import random


class Cipher:
    def __init__(self, number1, number2):
        self.__n1 = number1
        self.__n2 = number2

    def __calculate(self):
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            return self.__n1 + self.__n2
        elif operation == '-':
            return self.__n1 - self.__n2
        elif operation == '*':
            return self.__n1 * self.__n2
        elif operation == '/':
            return self.__n1 / self.__n2 if self.__n2 != 0 else 0

    def __str__(self):
        result = self.__calculate()
        return f"Результат шифрування: {result}"


my_cipher = Cipher(10, 5)

print(my_cipher)