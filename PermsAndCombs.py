import itertools

which = input("Permutations(order matters) or combinations (order doesn't) (type p or c)? ")
startnum = int(input("Start number: "))
endnum = int(input("End number: "))
length = int(input("Length: "))

if(which == 'p'):
    perm = list(itertools.permutations(range(startnum, endnum + 1), length))
    print("Here are your permutations: ")
    for i in list(perm):
        print(i)
    print("There are " + str(len(perm)) + " permutations")
elif(which == 'c'):
    comb = list(itertools.combinations(range(startnum, endnum + 1), length))
    print("Here are your combinations: ")
    for i in list(comb):
        print(i)
    print("There are " + str(len(comb)) + " combinations")
else:
    print("type p or c")
