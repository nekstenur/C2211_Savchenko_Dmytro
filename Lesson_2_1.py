import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 1500

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.money -= 35

    def to_sleep(self):
        print("I'll sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 225

    def to_repeat(self):
        print("I need to repeat")
        self.gladness -= 2
        self.progress += 0.04

    def cash_in(self):
        print("I need more money")
        self.money += random.randint(150, 450)
        self.gladness -= 1
        self.progress -= 0.01


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
        elif self.money <= -100:
            print("Dont have any money")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = f"Day {day}, of {self.name} life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_repeat()
        elif live_cube == 5:
            self.cash_in()
        #--result
        self.end_of_day()
        self.is_alive()


student1 = Student(name="Vasya")
student2 = Student(name="Shasha")

for day in range(365):
    if student1.alive:
        student1.live(day)
    if student2.alive:
        student2.live(day)
    if student2.alive == False & student1.alive == False:
        break



