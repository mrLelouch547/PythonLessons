constnum=0b1
n1=int(input("Въведи"))
n2=int(input("Позиция на проверка"))
constnum=constnum<<n2
check=constnum&n1
if(check!=0):
    print(str(n1)+" има единица нa позиция "+str(n2))
else:
    print(str(n1)+" няма единица в позиция "+str(n2))
