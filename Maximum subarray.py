'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach,
which is more subtle.
'''


def maximumSubarray(arr):
    maxSum = currentSum = arr[0]
    for i in range(1,len(arr)):
        currentSum = max(arr[i],currentSum+arr[i])
        maxSum = max(maxSum,currentSum)
    return maxSum


if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximumSubarray(arr))
