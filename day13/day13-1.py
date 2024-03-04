# opening the file 
with open("input13.txt", "r") as file : 
    data = file.read().strip().split("\n\n")

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
    

result = 0
for i in range(len(data)) : 
    line = data[i].split("\n")
    list_1, list_2 = map(eval,line)
    # if the two lists are sorted, we add 1 to the result
    if compare(list_1,list_2) == 1 :
        result += i+ 1

print("result :", result)
    
# result : 13 as expected with test.txt