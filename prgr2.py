#Er wordt vanuit gegaan dat er tussen 2 integers 1 komma wordt ingevoerd

c = input("Geef 2 getallen gescheiden door een komma: ")

c_lijst = c.split(",")

d = c_lijst[0]
e = c_lijst[1]

print(d==e)