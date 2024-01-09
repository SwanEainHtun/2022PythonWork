import re
fh = open("real1.txt")
x = list()
for line in fh:
    line = line.rstrip()
    y = re.findall('([0-9]+)',line)
    for z in y:
        x.append(int(z))
print(sum(x))
