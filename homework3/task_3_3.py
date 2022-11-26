import random

catalog = random.sample(range(-100, 100), 10)
print("список 1:", catalog)

catalog[2] = random.randrange(-100, 100)
del catalog[6]
print("список 2:", catalog)
