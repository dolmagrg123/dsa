'''
UNDERSTAND:

1. list of numbers
2. not too low not too high
3. write a function goldilocks_approved()
4. distinct positive integers nums as parameter
5. neither min nor max is returned
6. return -1 if no such number


PLAN

1. create function goldilocks_approved(nums)
2. if len(nums) <= 2, return -1
3. find the min and max value in the list -> min(nums) max(nums)
4. for each value in the list, check if it is min or max
5. if neither min or max, then return the value, elif look at the next number, else -1

IMPLEMENT

'''

def goldilocks_approved(nums):

    if len(nums) <= 2:
        return -1
    
    min_value = min(nums)
    max_value = max(nums)

    for val in nums:
        if val != min and val !=max:
            return val
    
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))




