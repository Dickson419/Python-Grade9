import time

numbers = [2, 4, 5, 6, 12, 45, 2, 1, 11, 67, 23, 90, 33]
numbers_two = [1, 3, 5, 8, 12, 13, 16, 21, 67, 78, 111, 204, 324]

# start = time.time()  # start the timer/stopwatch
# end = time.time() - start
# print("\nTime taken: {:.5f} seconds".format(end))

def binary_search(nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
        # find the midpoint (low + high) // 2
        mid = (low + high) // 2
        print(f"Midpoint: {mid}. High: {high}. Low: {low}\n")

        #three outcomes: found, target lower than mid, target high than mid
        if nums[mid] == target:
            print(f"Target {target} is located at {mid}")
            break
        elif target < nums[mid]:
            high = mid - 1
            print(f"High = {high}, Mid = {mid}")
        elif target > nums[mid]:
            low = mid + 1
            print(f"High = {high}, Mid = {mid}")

    # If we exit the loop, the target was not found
    if low > high:
        print(f"Target {target} not found in the list")


binary_search(numbers_two,3 )
