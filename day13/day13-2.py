# import the functools module
from functools import cmp_to_key

# opening the file 
with open("input13.txt", "r") as file : 
    # we change that to make suppress the lines that are empty to consider the file as a list of lines that need to be sorted 
    data = file.read().strip().replace("\n\n", "\n").split("\n")

# printing the data
print("data :")
for line in data : 
    print(line)
    print()

# function that compare wether two list are the same 
def compare(a,b) :
    # case where a is a number and b is a list
    if isinstance(a, int) and isinstance(b, list) :
        a=[a]

    # case where a is a list and b is a number
    if isinstance(a, list) and isinstance(b, int) :
        b=[b]

    # case where a and b are numbers
    if isinstance(a, int) and isinstance(b, int) :
        if a < b : 
            return 1
        if a == b :
            return 0
        return -1
    
    # case where a and b are lists
    if isinstance(a,list) and isinstance(b,list) :
        i = 0
        while i < len(a) and i < len(b) :
            x = compare(a[i],b[i])
            # if the two elements are equal we continue, because the tests will be skipped 
            # otherwise we now if it's sorted or not
            if x == 1 : 
                return 1
            if x == -1 :
                return -1
            i += 1
        
        if i == len(a) :
            # if the two lists are equal, we return 0
            if len(a) == len(b) :
                return 0
            # sorted because the terms of list a are all equal to the ones from b, but less in number
            return 1
        
        return -1 # if nothing has been returned, by now, the list isn't sorted
    

add_1=[[2]]
add_2=[[6]]
data=list(map(eval,data))
print(data)
data.append(add_1)
data.append(add_2)
# we sort the data with the compare function
data=sorted(data, key=cmp_to_key(compare), reverse=True)
    
result = 1
# result : 13 as expected with test.txt
for i in range(len(data)) : 
    if data[i] == add_1 : 
        result *= i+1
    if data[i] == add_2 :
        result *= i+1

print("result :", result)  

# we found 140 with test.txt as expected