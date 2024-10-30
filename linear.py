import time

numbers = [2, 4, 5, 6, 12, 45, 2, 1, 11, 67, 23, 90, 33]

def linear_search(nums, target):
    start = time.time()  # start the timer/stopwatch
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] == target:
            print("FOUND ", target, " at location ", i)
    end = time.time() - start
    print("\nTime taken: {:.5f} seconds".format(end))


linear_search(numbers, 2)


