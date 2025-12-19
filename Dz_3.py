import random

cat_breeds = {
    "Siamese": {"energy": 100, "claws_sharpness": 80, "hunger_rate": 7},
    "Persian": {"energy": 60, "claws_sharpness": 40, "hunger_rate": 4},
    "Street Cat": {"energy": 120, "claws_sharpness": 100, "hunger_rate": 10},
    "British Shorthair": {"energy": 80, "claws_sharpness": 60, "hunger_rate": 5}
}

role_list = {
    "Mouser": {"reward": 40, "tiredness": 15},
    "Lazy Pet": {"reward": 20, "tiredness": 2},
    "Night Screamer": {"reward": 10, "tiredness": 25},
    "Internet Star": {"reward": 100, "tiredness": 20}
}

class Cat:
    def __init__(self, name=""):
        self.name = name
        self.treats = 50
        self.happiness = 50
        self.satiety = 50
        self.role = None
        self.body = None
        self.territory = None

    def get_territory(self):
        self.territory = Territory()

    def get_body(self):
        self.body = CatBody(cat_breeds)

    def get_role(self):
        self.role = CatRole(role_list)

    def eat(self):
        if self.territory.bowl <= 0:
            self.beg_for_food()
        else:
            if self.satiety >= 100:
                print("I am full!")
                return
            self.satiety += 15
            self.territory.bowl -= 10

    def beg_for_food(self):
        print("Meow! Feed me, human!")
        if self.happiness > 10:
            self.treats += 10
            self.territory.bowl += 20
            self.happiness -= 5
        else:
            print("Human ignored me")

    def do_cat_things(self):
        if self.body.use_energy():
            self.treats += self.role.reward
            self.happiness += 10
            self.satiety -= 10
            print(f"I did some {self.role.name} stuff!")
        else:
            print("Too tired to move")
            self.sleep()

    def sleep(self):
        print("Zzz.. Sleeping all day")
        self.body.energy += 30
        self.happiness += 5
        self.satiety -= 5

    def sharpen_claws(self):
        print("Scratching the sofa!")
        self.body.claws += 50
        self.territory.mess += 20
        self.happiness += 15

    def clean_self(self):
        print("I am clean now")
        self.happiness += 5
        self.territory.mess -= 5

    def status(self, day):
        status_line = f" Day {day} of {self.name}'s cat life "
        print(f"{status_line:=^50}")
        print(f"Treats: {self.treats} | Happiness: {self.happiness} | Satiety: {self.satiety}")
        print(f"Energy: {self.body.energy} | Bowl: {self.territory.bowl} | Mess: {self.territory.mess}")

    def is_alive(self):
        if self.happiness < 0:
            print("The cat ran away from home")
            return False
        if self.satiety < 0:
            print("The cat is starving")
            return False
        if self.treats < -100:
            print("Human is too angry, no more treats")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.territory is None:
            self.get_territory()
        if self.body is None:
            self.get_body()
        if self.role is None:
            self.get_role()

        self.status(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.body.energy < 20:
            self.sleep()
        elif self.territory.mess > 40:
            self.clean_self()
        elif self.body.claws < 10:
            self.sharpen_claws()
        elif dice == 1:
            self.do_cat_things()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            print("Zoomies! Running around!")
            self.happiness += 20
            self.body.energy -= 15
        elif dice == 4:
            self.sharpen_claws()

class CatBody:
    def __init__(self, breeds):
        self.breed = random.choice(list(breeds))
        self.energy = breeds[self.breed]["energy"]
        self.claws = breeds[self.breed]["claws_sharpness"]
        self.burn_rate = breeds[self.breed]["hunger_rate"]

    def use_energy(self):
        if self.energy > 10:
            self.energy -= 10
            return True
        return False

class Territory:
    def __init__(self):
        self.bowl = 50
        self.mess = 0

class CatRole:
    def __init__(self, roles):
        self.name = random.choice(list(roles))
        self.reward = roles[self.name]["reward"]
        self.tiredness = roles[self.name]["tiredness"]

my_cat = Cat(name="Murzik")

for day in range(1, 365):
    if my_cat.live(day) == False:
        break