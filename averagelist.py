numlist = list()
while True:
    inp = input("Enter a number ")
    if inp == "stop":
        break;
    value = float(inp)
    numlist.append(value)
print("average is ",sum(numlist)/len(numlist))