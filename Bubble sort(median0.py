nums = [7, 2, 9, 4, 1, 6]

n = len(nums)


for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted list:", nums)
