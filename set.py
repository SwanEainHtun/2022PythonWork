utensils = {"fork","spoon","knife"}
newitem = input("Enter a new item plz!: ")
utensils.add(newitem)
for x in utensils:
    print(x)
dishes = {"bowl","plate"}
dishes.update(utensils)
print(dishes)
sorted(utensils)