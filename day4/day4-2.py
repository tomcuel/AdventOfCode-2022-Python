# I open the file and read the lines, then I split the lines to be able to treat them separetely 
with open("input4.txt", "r") as file:
    lines = file.read()[:-1].split("\n")

print()
# just a test to see the content of the file
print("raw lines",lines, "\n")

sum=0 
for line in lines : 
    # we separate what concerns the first and the second elf
    line=line.split(",")
    # print(line) # just a test to see the content of the file, that it has been split correctly
    # we are splitting the ranges of the elves to get the beginning and the end of the range, adding that to a list 
    ranges=[list(map(int,elf.split("-"))) for elf in line]
    # print("ranges",ranges) #just to see that it worked as intended 
    # first elf 
    a = ranges[0][0] # beginning 
    b = ranges[0][1] # end 
    # second elf 
    c = ranges[1][0] # beginning 
    d = ranges[1][1] # end 
    # we look if there is a crossing of the two range lists or one that is included in the others 
    if (b>=c and b<= d) or (a<=d and a>=c) or (c<=a and d>=b) or (c>=a and d<=b) : 
        sum+=1
        print(ranges)
    
print("\nle résutlat est ; ",sum,"\n")

# we found 4 for test.txt, as it was expected