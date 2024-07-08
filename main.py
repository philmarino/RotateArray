def rotateArray(list, steps):
    for step in range(steps):
        element = list[len(list)-1]
        list.pop(len(list)-1)
        list.insert(0, element)
    return

#Example 1:
#Input: 
nums = [1,2,3,4,5,6,7]
k = 3
rotateArray(nums, k)
print(nums)
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

#Example 2:
#Input: 
nums = [-1,-100,3,99]
k = 2
rotateArray(nums, k)
print(nums)
#Output: [3,99,-1,-100]
#Explanation: 
#rotate 1 steps to the right: [99,-1,-100,3]
#rotate 2 steps to the right: [3,99,-1,-100]
