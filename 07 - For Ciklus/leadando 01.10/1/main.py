user_input = 0
while True:
    print("Adja meg hány elemű a piramis: ", end="")
    user_input = input()

    if not user_input.isdigit():
        print("Nem számot adott meg")

    else:
        rows = int(user_input)
        for i in range(0,rows,1):
            for j in range(i + 1):
                print(j + 1, end=" ")
            if i < rows - 1:
                print(end="\n")
        break 