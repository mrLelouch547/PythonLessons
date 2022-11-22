nterms = int(input("Колко числа? :  "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Моля въведете положително число: ")
elif nterms == 1:
   print("Броят на числата на фибоначи",nterms,":")
   print(n1)
else:
   print("Редицата на финбоначи:")
   while count < nterms:
       print(n1)
       nth = n1 + n2    
       n1 = n2
       n2 = nth
       count += 1