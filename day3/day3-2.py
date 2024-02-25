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

dataset=[]
k=0
Temp=[]
for line in lines:
    Temp.append(line)
    k+=1
    if (k%3==0):
        dataset.append(Temp)
        Temp=[]

print("dataset : \n",dataset, "\n")

sum=0; 
for lines in dataset:
    a=lines[0]
    b=lines[1]
    c=lines[2]
    # we are looking for the common letters in the 3 strings, so we go through the letters 
    for i,d in enumerate(key):
        # looking if the letter is in each word 
        if d in a and d in b and d in c : 
            sum+=key.index(d)+1 #key is then a list of 52 letters, starting from 0 in terms of index, so the +1 to the sum i've added
    
# display the result 
print("The sum of the common characters is: ",sum, "\n")

# we found 70 as it was expected for the test.txt file 