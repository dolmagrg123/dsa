def make_divisible_by_3(nums):
    operations_num = 0

    for i in nums:
        while i % 3 != 0:
            operations_num += 1
            if i % 3 == 1:
                i -=1
            else:
                i+=1
    return operations_num

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))
