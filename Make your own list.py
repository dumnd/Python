creation = []
pushed = 0
version = 0
push = 0
status = "running"
change = 0
print('You can type "word" or "number" to make a word or a number list')
version = input("Enter the type of list: ")

if version == "number":

    while status == "running":
        print('Type "push" to add a value or "pop" to delete a value or type "finish" to show the list you have made.'
              '')

        change = input('Edit the list: ')

        if change == 'push':
            push = int(input("enter the value: "))
            creation.append(push)

        elif change == 'pop':
            if not creation:
                print("List is empty")
            else:
                print(creation.pop())

        elif change == 'finish':
            print(creation, sep='\n')
            break

elif version == "word":
    while status == "running":
        print('Type "push" to add a value or "pop" to delete a value or type "finish" '
              'to show the list you have made.')

        change = input('Edit the list: ')

        if change == 'push':
            push = (input("enter the word: "))
            creation.append(push)

        elif change == 'pop':
            if not creation:
                print("List is empty")
            else:
                print(creation.pop())

        elif change == 'finish':
            print(creation, sep='\n')
            break








