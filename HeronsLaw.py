import math

s1 = int(input("side 1: "))
s2 = int(input("side 2: "))
s3 = int(input("side 3: "))

halfsa = (s1 + s2 + s3)/2
Area = math.sqrt(halfsa*(halfsa-s1)*(halfsa-s2)*(halfsa-s3))
print(Area)

