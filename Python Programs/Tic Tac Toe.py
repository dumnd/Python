import random
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]
values = []
print("Respond in format:(row,column)")
place = 0
computer_row = 0
computer_column = 0
x = 0
y = 0
counter = 0
result = 0
while y == 0 :
    print("1", row1)
    print("2", row2)
    print("3", row3,)
    print("    1     2     3")
    response = (input("Where do you want to place your token: "))
    values = response.split(",")
    place = values[1]
    place = int(place)
    if values[0] == '1':
        row1[place - 1] = "O"
    if values[0] == '2':
        row2[place - 1] = "O"
    if values[0] == '3':
        row3[place - 1] = "O"
    while x == 0:
        computer_row = random.randrange(1,3)
        computer_column = random.randrange(0,2)
        if computer_row == 1:
            if row1[computer_column] == "-":
                row1[computer_column] = "X"
                x = 1
        if computer_row == 2:
            if row2[computer_column] == "-":
                row2[computer_column] = "X"
                x = 1
        if computer_row == 3:
            if row3[computer_column] == "-":
                row2[computer_column] = "X"
                x = 1
    counter = counter + 1
    if counter == 3:
        result = str(input("What happened: "))
        if result == "i lost":
            print("You lost the game")
            y = 1
        if result == "i won":
            print("Your score was", counter)
            y = 1
    x = 0





