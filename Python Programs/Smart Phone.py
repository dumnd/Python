people_num = int(input())
people = []
lower = []
prices = []
for x in range(0, people_num):
    sub = int(input())
    people.append(sub)

people.sort()
count = 0
for x in range(0, people_num):
    for y in range(0, people_num - count):
        lower.append(people[x])
    y = 0
    prices.append(sum(lower))
    lower.clear()
    count += 1
prices.sort()
print(prices[-1])


