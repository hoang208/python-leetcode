'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
'''

'''
Get product of every value before value in array, and get product of every value after value in array
Mutiple the products together
'''

# My Solution
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    prefix = [1] * (len(nums))
    postfix = [1] * (len(nums))

    for i in range(1, len(nums)):
      prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in reversed(range(len(nums)-1)):
      postfix[i] = postfix[i + 1] * nums[i + 1]

    return [prefix[i] * postfix[i] for i in range(len(nums))]

# Other Solutions
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
      ans[i] = prefix
      prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
      ans[i] *= postfix
      postfix *= nums[i]
    return ans