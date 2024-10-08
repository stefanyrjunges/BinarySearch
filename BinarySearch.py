import numpy as np

randomInt = np.random.randint(1000, size=100)
sorted_randoms = np.sort(randomInt)

length = len(sorted_randoms)

lowerIndex = 0
upperIndex = length - 1
found = False
count = 0

print(sorted_randoms)

query = int(input("Enter query: "))

while not found and upperIndex >= lowerIndex:
    midPoint = lowerIndex + (upperIndex - lowerIndex) // 2
    count += 1

    if sorted_randoms[midPoint] == query:
        print('Data found after ' + str(count) + ' iterations')
        found = True

    elif sorted_randoms[midPoint] > query:
        upperIndex = midPoint - 1

    else:
        lowerIndex = midPoint + 1

if not found:
    print('Data has not been found')

np.savetxt("myData.csv", sorted_randoms, delimiter=",")
