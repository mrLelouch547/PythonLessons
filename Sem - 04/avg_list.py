def list_avg(lst,multiplier=1):
    average = 0
    countnum = 0
    for element in lst:
        if type(element) == float or type(element) == int:
           average += element * multiplier
           countnum+=1
        if type(element) == str and element.isnumeric():
            average += int(element) * multiplier
            countnum += 1
    if countnum == 0:
        return "Error: Division by zero"
    return average/countnum

print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))
