dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}

dict3 = {}

for key, value in dict1.items():
    if dict1.get(key) != dict2.get(key):
        dict3[key] = [value, None]
    else:
        dict3[key] = [value, value]
for key, value in dict2.items():
    if dict1.get(key) != dict2.get(key):
        dict3[key] = [None, value]
print(f"dict3 = {dict3}")