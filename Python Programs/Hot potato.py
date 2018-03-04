players = []
import random
counter = "yes"
potato = 0
while counter == "yes":
    counter = str(input("Type player name :"))
    players.append(counter)
    counter = str(input("type yes if you want another player or no if you don't: "))

counter = 0
name = 0

while len(players) > 1:
    x = random.randrange(1, 50)
    if counter >= len(players):
        counter = 0
    name = players[counter]
    if x%3 == 0:
        del players[counter]
        print(name, "is out")

    counter = counter + 1

print(players[0],"is the winner")






