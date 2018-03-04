cases = int(input())
words = []
for x in range(0, cases):
    words.append(str(input()))

for y in range(0, cases):
    if y == cases - 1:
        for z in range(0, cases):
            counter = words.count(words[z])
            if counter > 1:
                if (y + 1) % 2 == 0:
                    print("Player 2 lost")
                    exit()
                if (y + 1) % 2 != 0:
                    print("Player 1 lost")
                    exit()
        print("Fair Game")
        exit()
    a = words[y]
    b = words[y + 1]
    if a[-1] == b[0]:
        continue
    elif (y + 1) % 2 == 0:
        print("Player 1 lost")
        exit()
    elif (y + 1) % 2 != 0:
        print("Player 2 lost")
        exit()
