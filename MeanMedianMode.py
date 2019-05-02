import statistics
data = input("Enter your space separated numbers: ")
dataArr = data.split(' ')
dataArr = list(map(int, dataArr))
dataArr.sort()
print("Mean: " + str(statistics.mean(dataArr)))
print("Median: " + str(statistics.median(dataArr)))
print("Mode: " + str(statistics.mode(dataArr)))
print("Your sorted data: " + str(dataArr))
