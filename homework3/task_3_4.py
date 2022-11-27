from itertools import chain


def mergeDict(dict1, dict2):
    for k, v in chain(dict1.items(), dict2.items()):
        if dict1.get(k):
            dict1[k] = [v, v]
        else:
            dict1[k] = [None, v]
    return dict1


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}

print(dict1)
print(dict2)

dict3 = mergeDict(dict1, dict2)

print(dict3)
