def input_nums(num):
    list = []
    if type(num) == num or (type(num)==str and num.__str__().isnumeric()):
        for i in range(int(num)):
            number = input("Въведете за N - ")
            if type(number) == int or (type(number) == str and number.__str__().isnumeric()):
                list.append(int(number))
    return list

def sum_list(lst):
    sum = 0
    for element in lst:
        if type(element) == int or type(element) == float:
            sum += element
        elif type(element) == str and element.isnumeric():
            sum += float(element)
    return sum

def max_of_two(a, b):
    if (type(a) == int or type(a) == float) and (type(b) != int or type(b) != float):
        return a
    elif (type(b) == int or type(b) == float) and (type(a) != int or type(a) != float):
        return b
    elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a > b:
        return a
    elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a < b:
        return b
    elif (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float) and a == b:
        return a
    else:
        return

print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
