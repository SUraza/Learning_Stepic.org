x = [
    ("Guido", "van", "Rossum"),
    ("Haskel", "Curry"),
    ("John", "Backus")
]

#def lenght(name):
#    return len(" ".join(name))

#name_lenghts = [lenght(asd) for asd in x]
#print(name_lenghts)

#x.sort(key=lambda asd: len(" ".join(asd)))
#print(x)

import operator as O
x.sort(key=O.itemgetter(-1))
print(x)
