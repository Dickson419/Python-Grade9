import time

my_numbers = [1, 5, 2, 7, 10, 23, 4, 2]

print("len(my_numbers): ", len(my_numbers), " items in the array")
print("len(my_numbers) -1: ", len(my_numbers)-1, " indexes (they start at 0)")
#print(my_numbers[0])
print("\n")

start = time.time() #start the timer/stopwatch

# iterate through all array elements
for i in range(len(my_numbers)-1):
    min_index = i #start at index 0, increment with each loop

    for j in range(i + 1, len(my_numbers)):
        if my_numbers[j] < my_numbers[min_index]:
            min_index = j #the element (index location) being compared IF smaller is changed to the new min index
    #outside of IF perform the swap as new smallest item is found
    my_numbers[i], my_numbers[min_index] = my_numbers[min_index], my_numbers[i]

end = time.time() - start


print(my_numbers)
print("\nTime taken: {:.5f} seconds".format(end))
