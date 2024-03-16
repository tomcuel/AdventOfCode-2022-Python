from tqdm import tqdm

# opening the file 
with open("input20.txt", "r") as file : 
    lines=file.read().strip().split("\n")

# converting the list of strings to list of integers
for i, line in enumerate(lines):
    lines[i]=int(line)
# printing the input
# print("input :",lines,"\n")

# length of the input, to be quicker to access
n=len(lines)

# function to swap two elements of the list
def swap(lines, i, j):
    assert (0 <= i < n) and (0 <= j < n)

    lines[i], lines[j] = lines[j], lines[i]
    return lines

# function that find the index of the element in the list
def find_index(lines, number_to_find):
    for i in range(len(lines)):
        if lines[i]==number_to_find:
            return i
    return -1

nums=lines.copy()
# tqdm to see the progress of the loop 
for i in tqdm(range(n)):
    # print("round",i+1)
    number_to_move=lines[i]
    number_to_move_index=find_index(nums, number_to_move)
    # print("number to move :", number_to_move)


    # don't have to do anything in the case of 0
    if number_to_move==0:
        # print("nums after the round :",nums,"\n")
        continue


    # if the number is positive, we move it to the right
    if number_to_move>0:
        move_made=0
        # making the right amount of moves
        while move_made<number_to_move:
            
            # finding the index of the number to move
            index=find_index(nums, number_to_move)
            # print("index : ",index)

            # if the index is not the last one, we swap the number with the next one
            if index < n-1 : 
                nums=swap(nums, index, index+1)
                # print("nums :",nums)
                move_made+=1
                # print("move_made : ",move_made) 

            # if the index is the last one, we swap the last number with the second to last, and so on
            if index == n-1:
                for j in range(n-1):
                    nums=swap(nums, n-1-j, n-j-2)
                # print("nums :",nums)
                # print("move_made : ",move_made)


    # if the number is negative, we move it to the left
    if number_to_move<0:
        move_made=0
        # the number to move is the opposite of the number to move
        # if the number to move is -3, we move n-3 times to the right, since it's the same as moving 3 times to the left
        number_to_move_inverted=n-1-abs(number_to_move)
        while move_made<number_to_move_inverted:

            # finding the index of the number to move
            index=find_index(nums, number_to_move)
            # print("index : ",index)
            
            # if the index is not the last one, we swap the number with the next one
            if index < n-1 : 
                nums=swap(nums, index, index+1)
                # print("nums :",nums)
                move_made+=1
                # print("move_made : ",move_made) 

            # if the index is the last one, we swap the last number with the first one
            if index == n-1:
                nums=swap(nums, index, 0)
                # print("nums :",nums)
                move_made+=1
                # print("move_made : ",move_made)


    # print("nums after the round :",nums,"\n")

print("nums after the rounds :",nums,"\n")

# the 3 index we want to find the sum of the numbers that are at these indexes
coords=[1000,2000, 3000]

# finding the index of the 0
zero_index=find_index(nums,0)
# print("zero_index : ",zero_index,"\n")
# to be sure we get the 1000th, 2000th and 3000th number after the first 0

index_of_1000=(zero_index+1000)%n
index_of_2000=(zero_index+2000)%n
index_of_3000=(zero_index+3000)%n

# finding the numbers at the indexes we want
first_zero=nums[index_of_1000]
seconde_zero=nums[index_of_2000]
third_zero=nums[index_of_3000]
print("first_zero : ",first_zero)
print("seconde_zero : ",seconde_zero)
print("third_zero : ",third_zero)

# summing the numbers
answer=first_zero+seconde_zero+third_zero
print("\nanswer : ",answer,"\n")

# we found 3 as expected for the test.txt file

# not great for input20.txt because it didn't consider there could be many times the same number in the list
# I will fix that 
