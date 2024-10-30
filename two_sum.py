

"""
You are given an array arr[] of n integers and a target value.

The task is to find whether there is a pair of elements in the array whose sum is equal to target.

EXAMPLE INPUT
arr = [2, 4, 5, 6]
target = 9
"""

def two_sum(arr, target):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                print("FOUND numbers ", arr[i] , arr[j], " = target ", target )

numbers = [2, 4, 5, 6]
two_sum(numbers, 9)