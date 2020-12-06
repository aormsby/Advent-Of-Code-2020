nums = []
results1 = []

with open("input.txt") as input:
    for i in input.readlines():
        nums.append(int(i.strip("\n")))

for n in nums:
    for i in range(len(nums)):
        if n + nums[i] == 2020:
            results1.append(n)
            results1.append(nums[i])
            break
    else:
        continue
    break

# result 1: product of nums that sum to 2020
print("result 1: " + str(results1[0] * results1[1]))

results2 = []
nums.sort()

for x in range(0, len(nums)):
    left = x + 1
    right = len(nums) - 1

    while (left < right):
        if nums[x] + nums[left] + nums[right] == 2020:
            results2.append(nums[x])
            results2.append(nums[left])
            results2.append(nums[right])
            break
        elif nums[x] + nums[left] + nums[right] < 2020:
            left += 1
        else: # nums[x] + nums[left] + nums[right] > 2020
            right -= 1
    else:
        continue
    break

print("result 2: " + str(results2[0] * results2[1] * results2[2]))