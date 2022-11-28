numlist = []
n = int(input('Брой числа: '))
for i in range(n):
    num = int(input('Въведете число: '))
    numlist.append(num)
option = int(input('Въведете 0 или 1: '))
if option == 0:
    for i in range(0,len(numlist),2):
        if i % 2 == 0:
            numlist[i]+= 5
elif option == 1:
    for i in range(1,len(numlist),2):
        if i % 2 != 0:
            numlist[i]+=10
else:
    print('Невалидна команда!')
print(f'новият списък е {numlist}!')
