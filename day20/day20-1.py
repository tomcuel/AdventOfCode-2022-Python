# to see the progress of the loop
from tqdm import tqdm

# opening the file 
with open("input20.txt") as fin:
    lines = fin.read().strip().split("\n")
    # converting the list of strings to list of integers and getting its index, thanks to enumerate
    nums = list(enumerate(map(int, lines)))

print("input :", nums, "\n")
# length of the input, to be quicker to access
n = len(nums)
# copying the list to not modify the original one
# we will use the copy make the round for each numbers in the order of the input 
copy_nums = nums.copy()


# function to swap two elements of the list
def swap(nums, a, b):
    assert (0 <= a < n) and (0 <= b < n)

    nums[a], nums[b] = nums[b], nums[a]
    return nums


# tqdm to see the progress of the loop 
# going through the list of numbers of the copy to get them in the right order
# i is the index of the number, x is the number = number_of_moves to be made
for i, x in tqdm(copy_nums):
    # searching for the index of the number in the list
    for idx in range(n):
        if nums[idx][0] == i:
            break

    # checking if the index is correct, so that the numbers is the one corresponding to the index
    assert nums[idx][1] == x
    # print("index : ",index, "number : ",x)

    # if the number is positive, we move it to the right
    if x > 0:
        cur = idx
        for _ in range(x):
            # formula with % to get the right index, going in index 0 after the last index
            nums = swap(nums, cur, (cur + 1) % n)
            cur = (cur + 1) % n
    
    # if the number is negative, we move it to the left
    if x < 0:
        cur = idx
        for _ in range(-x):
            # formula with % to get the right index, going in the last index after index 0
            nums = swap(nums, cur, (cur - 1) % n)
            cur = (cur - 1) % n

        continue

    
print("output :", nums, "\n")

printed=[0 for _ in range(n)]
for i, x in nums:
    printed[i]=x
print("nums after the round :",printed,"\n")

# the 3 index we want to find the sum of the numbers that are at these indexes
coords = [1000, 2000, 3000]


# finding the index of the first 0
for zero_idx in range(n):
    if nums[zero_idx][1] == 0:
        break
# print("zero_index : ",zero_index,"\n")
# to be sure we get the 1000th, 2000th and 3000th number after the first 0

answer = 0
for c in coords:
    print(nums[(zero_idx + c) % n][1])
    answer += nums[(zero_idx + c) % n][1]

print("\nanswer : ",answer,"\n")

# we found 3 as expected for the test.txt file

# day20-1_no_for_… not great for input20.txt because it didn't consider there could be many times the same number in the list
# I fixed that in this one 
# by considering that there could be many times the same number in the list
# All that was needed was to get couples of indexes and numbers, so that we konw the index of each number, whether it's the first time we see it or not
