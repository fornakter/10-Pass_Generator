import random
tablica = []
#0-9
for i in range(48, 58):
    tablica.append(chr(i))
#A-Z
for i in range(65, 91):
    tablica.append(chr(i))
#a-z
for i in range(97, 123):
    tablica.append(chr(i))
print(tablica)
a = input("Ile ma byc znakow?: ")

for i in range(int(a)):
    b = random.randrange(len(tablica))
    print(tablica[b], end="")