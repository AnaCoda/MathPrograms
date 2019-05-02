m = int(input("m: "))
n = int(input("n: "))

print("The greatest integer that cannot be written in the form am + bn is: " + str(m * n - m - n))
print("There are " + str(((m-1)*(n-1))/2) + " positive integers which cannot be expressed in the form am + bm")
