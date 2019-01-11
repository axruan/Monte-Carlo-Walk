import random as r

l = [-1, 1]

home = 0

for i in range(0, 1000):

    x = 0
    y = 0

    for j in range(0, 10):
        dir1 = r.randint(1, 2)
        if dir1 == 1:
            dir2 = r.choice(l)
            x += dir2
        else:
            dir2 = r.choice(l)
            y += dir2

    dist = abs(x) + abs(y)
    if dist <= 4:
        home += 1

pct = str((home/1000)*100) + "%"
print("You made it home " + pct + " of the time")