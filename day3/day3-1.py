# importing the ascii_lowercase and ascii_uppercase from the string module
# to be able to make number of the letters
from string import ascii_lowercase, ascii_uppercase
key = ascii_lowercase + ascii_uppercase
print(key)

# I open the file and read the lines, then I split the lines to be able to treat them separetely 
with open("input3.txt", "r") as file:
    lines = file.read().strip().split("\n")

print()
# just a test to see the content of the file
print("lines non split",lines, "\n")
 
sum=0; 
for line in lines:
    # I use the set function to split the lines in half 
    n=len(line)
    mid=n//2
    a=line[:mid] # first half of the line
    b=line[mid:] # second half of the line
    for i,c in enumerate(key):
        # looking if the letter is in each word 
        if c in a and c in b : 
            sum+=key.index(c)+1 #key is then a list of 52 letters, starting from 0 in terms of index, so the +1 to the sum i've added
    
# display the result 
print("The sum of the common characters is: ",sum, "\n")

# we found 157 as it was expected for the test.txt file 