# opening the file 
with open("input6.txt", "r") as file : 
    line=file.read()

# just to see we get the right thing : 
print("line :\n",line, "\n")

i=0; 
# while we don't find the 4 letters that are different and following each other
while True :
    # we take 4 letters and check if they are all different
    s=line[i:i+4]
    if len(set(s)) == 4 :
        print("the result is :",4+i,"\n")
        break
    # if there are different we move to the next 4 letters
    i+=1

# the result is 4 for test.txt as expected