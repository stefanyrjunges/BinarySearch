import numpy as np

#Storing random integers
#99 random integers from 0-1000
randomInt = np.random.randint(1000, size=100)
#Sorting the randoms in order
sorted_randoms = np.sort(randomInt)
#Stored in a variable the length of the random integers after being sorted 
length = len(sorted_randoms)

lowerIndex = 0
#Using the variable length to get the last index. 100-1 = 99
upperIndex = length - 1
found = False
count = 0

#Checking if the number is here so I can test the functionality
print(sorted_randoms)

#Ask user for input (number in this case)
#Converting to int because otherwise it will be a string
query = int(input("Enter query: "))

#looping through the numbers
#upperIndex has to be >= than lowerIndex because it changes value later (see:upperIndex = midPoint - 1 for example)
#If upperIndex < lowerIndex for example, that means all the numbers have been analysed
while not found and upperIndex >= lowerIndex:
        #Finding middle number in the "array" (midPoint will be an index)
        midPoint = lowerIndex + (upperIndex - lowerIndex) // 2 
        #Count goes up every iteration so we can display to the user later
        count += 1

        #If the middle number is the same as the user input
        if sorted_randoms[midPoint] == query:
            #Had to convert count to a string because int cant be in the same place as strings
            print('Data found after ' + str(count) + ' iterations')
            found = True

        #If the middle number index is > than user input
        elif sorted_randoms[midPoint] > query:
            #Analyse numbers higher than middle number
            upperIndex = midPoint - 1
            
        #If the middle number index is < than user input
        else:
            #Analyse numbers lower than middle number
            lowerIndex = midPoint + 1
            
            #I did this before but the first IF already checks that:
            #If the number analysed is the same as the user input
            #if (lowerIndex == query):
            #   print('Data found after ' + count + 'iterations')
            #   found = True
    
#If user input couldnt be found inside the "array"
if not found:
    print('Data has not been found')

np.savetxt("myData.csv", sorted_randoms, delimiter=",")