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
        return {'Name': self.name, 'Nickname': self.nickname, 'Age': self.age, 'Eyes_color': self.eye}

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return int(self.age) < int(other.age)

    def __le__(self, other):
        return int(self.age) <= int(other.age)


def users_generator(number):
    num = 1
    while num <= number:
        name = random.choice(AVAILABLE_NAMES)
        nickname = name + str(random.randrange(10000, 100000))
        age = random.randrange(1, 100)
        eye = random.choice(AVAILABLE_COLORS)
        user = name, nickname, age, eye
        yield user
        num += 1
        continue
    


gen = users_generator(3)
for name, nickname, age, eye in gen:
    user = User(name, nickname, age, eye)
    print(user.info)
    print(type(user))

