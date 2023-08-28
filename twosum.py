# Return indices
# Assumption, assumption the array will never be empty
# constraint: Not use the same element

# a + b  = c
# b = c - a 

# 1. traverse the whole array
# 2. check for a possible correct value that sum up to target(b)
#     b = c - a
# 3. check if b is in nums
# 4. if not increment the index
# 5. if found then return indices of the two values
# 6. [1,2] ? [index of that elements]

#space complexity O(2) or O(1)
# time complexity O(1+1+n+1+1) => O(N) 1,2...n, O(1), O(log N),

def twoSum(nums, target):
       index = 0
       length = len(nums)

       if(length == 2):
            return[0,1]
       else:  
        while index < length:
            possibleCorrectValue = target - nums[index]
            if possibleCorrectValue in nums and nums.index(possibleCorrectValue) != index:
                return [index, nums.index(possibleCorrectValue) ]
            index += 1

sample = [1,2,1, 8,4,7]
target = 12

print(twoSum(sample,target))