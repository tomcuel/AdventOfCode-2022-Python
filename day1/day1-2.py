# Opening the file in read mode
with open('input1.txt', 'r') as file:
    # extracting the lines 
    lines = file.read().strip().split('\n\n')

# converting the list of strings to list of lists
data_char = []
for line in lines:
    # Splitting the lines by '\n' and appending to the data list
    data_char.append(line.split('\n'))

#print("list that is char",data_char)

# converting the list of strings to list of integers
data_int = []
for i in range(len(data_char)):
    data_int.append([int(j) for j in data_char[i]])

#print("list that is int",data_int)

# function to calculate the sum of the elements of a list
def sum (list) : 
    sum = 0
    for i in list:
        sum += i
    return sum

# function to calculate the top three sum of the elements of a list
def top_three_sum (data) : 
    maxs= [0,0,0]
    for i in range(len(data)): 
        # we search if sum(data[i]) is greater than the third elements of the list which is the smallest
        if sum(data[i]) > maxs[2]:
            # append the sum of the elements of the list to the maxs list
            maxs.append(sum(data[i]))
            # sort the list in descending order
            maxs.sort(reverse=True)
            # pop the last element of the list which will be the smallest
            maxs.pop()
    print("le résultat est",maxs[2]+maxs[1]+maxs[0])

top_three_sum(data_int)

# I did find 45000 for the test.txt file example