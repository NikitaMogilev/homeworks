import random
AVAILABLE_NAMES = ['John', 'Jane', 'Mary', 'David', 'Alex', 'Max', 'Nick', 'Anastasia', 'Leo']
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']


class User:

    def __init__(self, name, nickname, age, eye):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eye = eye

    @property
    def info(self):
        return print({'Name': self.name, 'Nickname': self.nickname, 'Age': self.age, 'Eyes_color': self.eye})

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return int(self.age) < int(other.age)

    def __le__(self, other):
        return int(self.age) <= int(other.age)


def users_generator(number):
    num = 0
    while num <= number:
        name = random.choice(AVAILABLE_NAMES)
        nickname = name + str(random.randrange(10000, 100000))
        age = random.randrange(1, 100)
        eye = random.choice(AVAILABLE_COLORS)
        user = {'Name': name, 'Nickname': nickname, 'Age': age, 'Eyes_color': eye}
        yield user
        num += 1
        continue


users = users_generator(1000000)
for user in users:
    print(user)
