first = str(input())
a, b = first.split()
a = int(a)
b = int(b)
tang = 0
obstacles = []
for x in range(0, b):
    obstacles.append(int(input()))
for y in range(0, a):
    tang = 0
    for z in range(0, b):
        if obstacles[z] == y:
            tang = 1
            continue
    if tang == 0:
        print(y)
b = str(b)
print("Mario got", b, "of the dangerous obstacles.")