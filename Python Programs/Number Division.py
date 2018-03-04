print("This will tell you what your number is divisible by")
magicnumber = int(input("Enter your magic number: "))

# number division

for x in range(1, 100):
    if magicnumber % x == 0:
        print(magicnumber, "is a multiple of", x)
    else:
        print(magicnumber, "is not a multiple of", x)

