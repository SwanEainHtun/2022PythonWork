import random
a = lambda x : x*2
print(a(40))
def myfun(n):
    return lambda b : b*n
mydoubler = myfun(2);
print(mydoubler(5))
mytripler = myfun(3)
print(mytripler(5))

kpop = ["EXO","NCT","Black Pink","Twice","2NE1","Loona","Red Velvet","StayC","Stray kids","Mamamoo"]
kpop.sort()

print(kpop)
print("-------------------------------------------")
def choose():
    z = random.choice(kpop)
    return z

print(choose())
