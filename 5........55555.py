number = int(input("Въведи: "))
a = 0
for j in range(1,number+1):
    p = str(number)*j
    if j < number:
        print(f"{p} +",end = " ")
    else:
        print(p,end=" ")
    a += int(p)
print("=", a)