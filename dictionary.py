dictionary = dict()
i = 0
num = int(input('Въведете число: '))
while i < num:
    key = input('Въведте стойност за ключа: ')
    value = input('Въведете стойност на ключа: ')
    dictionary[key] = value
    i+= 1
m = int(input('Въведете число за m: '))
k = 0
mlist = list()
while k < m:
    mvalue = input('Въведете стоност: ')
    if mvalue in dictionary.keys():
        mlist.append(dictionary[mvalue])
        dictionary.pop(mvalue)
    else: 
        mlist.append(mvalue)
    k += 1

print(dictionary)
print(mlist)
