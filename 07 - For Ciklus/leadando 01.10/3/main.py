user_input = 0
while True:
    print("Adja meg hány elemű a piramis: ")
    user_input = input()
    
    if not user_input.isdigit():
        print("Nem számot adott meg.")
        
    else:
        rows = int(user_input)
        num = 1
        for i in range(1, rows + 1):
            for _ in range(rows - i):
                print(" ", end="  ")
            for j in range(1, i * 2):
                print(f"{num:2}", end=" ")
                num += 1
            num = 1
            print()
        break