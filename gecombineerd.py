#PROGRAMMA 1:
#Er wordt vanuit gegaan dat er integers worden ingevoerd

a = int(input("Eerste getal is: "))
b = int(input("Tweede getal is: "))

print(a==b)


#PROGRAMMA 2:
#Er wordt vanuit gegaan dat er tussen 2 integers 1 komma wordt ingevoerd

c = input("Geef 2 getallen gescheiden door een komma: ")

c_lijst = c.split(",")

d = int(c_lijst[0])
e = int(c_lijst[1])

print(d==e)


#EXCEL SHEET:
#Ik heb online gekeken hoe ik excel sheets importeer naar Python

import pandas as pd

data = pd.read_excel("IsGelijk.xlsx")
print(data)