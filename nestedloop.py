rows = int(input("Enter rows numbers : "))
columns = int(input("Enter columns numbers : "))
symbol = input("Enter symbol : ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()