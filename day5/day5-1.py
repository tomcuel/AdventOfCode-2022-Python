# it could be easily done to get those by looking where to find it in the file but this was faster 
high_crates=8
print("height of the highest crates :\n",high_crates, "\n")
n_crates=9
print("number of crates :\n",n_crates, "\n")

# I open the file and read the lines, then I split the lines to be able to treat them separetely 
with open("input5.txt", "r") as file:
    lines = file.read()[:-1].split("\n\n") # we read beginning to end not to miss the first line spaces that could mess up our datas treatment
    # the stacks and the instructions are separated by a double line break, so we split the file by double line breaks and select which one is which 
    crates=lines[0].split("\n") # we separate the crates by lines
    print("crates :\n",crates, "\n")

    # we create a list of lists to put the stacks of the crates in
    stacks=[[] for _ in range (n_crates)]

    # we now try to put in a list the stacks of the crates by taking the datas from the lines
    for i in range(high_crates):
        line=crates[i]
        crate=line[1::4] # we just get the letter and not the [] anymore
        #print("crate",i,":",crate)
        for k in range(len(crate)):
            if crate[k]!=" ":
                stacks[k].append(crate[k]) # we make sure to put the letters in the right stack by using the index of the letter in the crate

# the probleme here is that our stacks are reversed and we need to reverse them again to get the right order
#print("stacks :\n",stacks, "\n")
stacks=[stack[::-1] for stack in stacks]
print("stacks reversed :\n",stacks, "\n")

# selecting the instructions by lines 
instructions=lines[1].split("\n") 
#print("instructions :\n",instructions, "\n")
# going through the instructions
for line in instructions : 
    tokens=line.split(" ")
    number, source, destination =map(int,[ tokens[1], tokens[3], tokens[5] ])# just by seeing how the file is written we can get the right indexes
    source -=1  # we need to remove 1 to the index to get the right index
    destination -=1 # we need to remove 1 to the index to get the right index
    #print("number, source, destination :",number, source, destination)
    # we will pop the letter on top of the stack and add it to the destination stack for the number of iterations needed
    for _ in range(number):
        pop = stacks[source].pop()
        stacks[destination].append(pop)

tops = [stack[-1] for stack in stacks]
print("".join(tops))

# the output is : CMZ as it was expected with the test file test.txt
# we need to put n_crates=3 and high_crates=3 to get the right output for test.txt