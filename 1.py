import math

y = 0
x = input("x")
z = input("z")

#number 1
if x > -math.pi and x < math.PI / 4:
    y = -(math.pow(math.cos(x), 2)) * (x - math.pi)
elif x >= math.pi / 4 and x <= 1:
    y = math.sqrt(math.fabs(x + 1))
else:
    y = 1 / (x - 1)
print(y)

#number 2
if math.fabs(x * z) < 1 and x < 0:
    y = x + z / (math.pow(math.e, x * z))
elif x > 2 and z <= 0:
    y = -(math.pow(math.log(x)))
elif z > 0 and x >= 0 and x <= 2:
    y = math.log(math.sqrt(z))
else:
    y = ""
print(y)

#number 3
if x >= 0 and x < 2:
    y = math.sqrt(math.fabs(x - 5,4))
elif x >= 2 / 4 and x < 8:
    y = math.pow(math.atan(x), 2)
else:
    y = math.log(math.fabs(x - 7,8))
print(y)
