user_input = 0 
while True:
    print("Adja meg hány elemű a piramis: ",end="")
    user_input =input()

    if not user_input.isdigit():
        print("Nem számot adott meg.")
        
    else:
        rows = int(user_input)
        for i in range(rows, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()
        break  
