import unittest
import time
import logging

logging.basicConfig(level=logging.INFO)

def check_speed(func, number):
    start = time.time()
    result = func(number)
    end = time.time()
    logging.info(f"Час роботи: {end - start} сек.")
    return result

def make_list(n):
    return [x for x in range(n)]


def make_gen(n):
    return (x for x in range(n))
class MyTest(unittest.TestCase):

    def test_list(self):
        res = check_speed(make_list, 5)
        self.assertEqual(len(res), 5)

    def test_gen(self):
        res = check_speed(make_gen, 10)
        self.assertEqual(type(res).__name__, 'generator')

if __name__ == '__main__':
    unittest.main()