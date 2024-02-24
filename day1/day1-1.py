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

# function to calculate the maximum sum of the elements of a list
max = 0 
for i in range(len(data_int)): 
    if sum(data_int[i]) > max:
        max = sum(data_int[i])

print("le résultat est",max) 

# it does print 24000 for the test.txt exampke