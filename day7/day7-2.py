from collections import defaultdict

# opening the file 
with open("input7.txt", "r") as file:
    # we split the file into blocks by direction and showing the blocks
    # thanks to the $ sign
    # we add \n to be able to split that later on
    blocks=("\n" + file.read().strip()).split("\n$ ")[1:]
    # note : we would have ' ' in the blocks if we used the following line :
    #  blocks=(file.read().strip()).split("$")[1:]
    # we should have proceed to change that but it will have taken more time

# make sure we get it 
#print(blocks,"\n")
print("blocks: \n")

# list giving the paths in the current folder 
path=[]
# directory sizes and its childrens in the tree 
# we use a defaultdict to avoid the key error, it is initialized to 0 for the keys that are not in the dictionary
directory_size=defaultdict(int) 
children=defaultdict(list)

# function that is going to analyze the blocks to decide what to do
# there are two cases : 
# 1. the block is a command of type cd 
# 2. the block is a command of type ls
# different actions are going to be taken depending on the type of command
def parse(block):
    lines=block.split("\n")
    print(lines) # to see it 
    command=lines[0] # the first line is the command (cd or ls)
    output=lines[1:] # skip the command part, and take the rest
    movement=command.split(" ") # split the command to be able to analyze it
    #print(movement) # to see it
    ope=movement[0] # the first part of the command is the operation, the second part is the direction taken in case of cd command
    if ope=="cd" :
        # we look if the movement is to go back to the parent directory
        if movement[1]==".." :
            path.pop()
        # or if the movement is to go to a specific directory
        else : 
            path.append(movement[1])
            print("path :",path) # to see it
        return # we've done enough for the block of type cd
    
    abspath="/".join(path) # to get the absolute path of the current directory
    #print(abspath) 
    assert ope=="ls" # we should have only ls commands by now 

    sizes=[]
    for line in output : # we look among the file that are shown by the ls command 
        print("file in that path :",line) # to see it
        # if the part we are looking at is not a directory, to take its size 
        if not line.startswith("dir") :
            sizes.append(int(line.split(" ")[0])) # we take the size of the file, that is the first string in for example : "2557 g"
        else : 
            dir_name = line.split(" ")[1] # we take the name of the directory
            children[abspath].append(f"{abspath}/{dir_name}") # we add the directory to the children of the current directory      

    directory_size[abspath]=sum(sizes) # we add the size of the files in the current directory to the directory_size dictionary

# we apply the function we designed to each block
for block in blocks :
    parse(block)

print("\n")
print("size of the directories : \n",directory_size,"\n")
# we have the list of the size of the different directories
print("children, differents places where there are files : \n",children,"\n")
# we have the structure of the tree of directories

# deepth first search to get the size of the directories by exploring the tree of paths we ceated 
# not the complete algorithm but just the exploration 
# sum the size of the directories given a path taken as input
def dfs(abspath):
    # take the size of the current directory
    size = directory_size[abspath]
    # take the size of the children directories to the current directory by exploring them
    for child in children[abspath]:
        size += dfs(child)
        # we add the size of the directories even if we need to take them many times 
    return size

# unused space in the system 
unused = 70000000 - dfs("/")
print("unused space : ", unused,"\n")
# required space of the system to run the update, it will need to be positive
required = 30000000 - unused
print("required space : ", required,"\n")

delete_directory_needed_size=70000000
# we look into the different directories 
for abspath in directory_size:
    # we take the size of the directories we are in 
    size=dfs(abspath)
    # if the size is enough to make the update, we take it
    if size >= required:
        # to suppress the least possible 
        delete_directory_needed_size=min(delete_directory_needed_size,size)

# we print the result
print("the result is : ", delete_directory_needed_size,"\n")

# we find 24933642 as expected with the test.txt file