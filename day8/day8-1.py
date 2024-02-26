import numpy as np

# opening the file
with open("input8.txt", "r") as file :
    lines = file.read().strip().split("\n")

# printing the lines just to check
print("file lines : \n",lines, "\n")

# making those datas integer to be able to manipulate them
datas = [list(map(int,(line))) for line in lines]
datas = np.array(datas)
n=len(datas)
m=len(datas[0])

# printing the data just to check
print("datas in integer :\n",datas,"\n")

sum=0
# checking if the tree is visible from all 4 sides
for i in range(n) :
    for j in range(m) :
        height=datas[i][j] # height of tree at i,j

        # different conditons to check if the tree is visible from all 4 sides
        # we need to differentiate according to the edge of the grid because then it will be seen
        # considering seeing from each edge of the grid correspond to a direction (up, down, left, right) to move in the grid, so we can join those conditions in a single one
        
        # moving from the left to the right (i fixed)
        if j == 0 or np.amax(datas[i, :j]) < height :
            sum+=1
        # moving from the right to the left (i fixed)
        # if we are not a the edge, we muss check if the max is a the edge, so the +1
        elif j == m-1 or np.amax(datas[i, (j+1):]) < height : 
            sum+=1
        # moving from the top to the bottom (j fixed)
        elif i == 0 or np.amax(datas[:i, j]) < height :
            sum+=1
        # moving from the bottom to the top (j fixed)
        # if we are not a the edge, we muss check if the max is a the edge, so the +1
        elif i == n-1 or np.amax(datas[(i+1):, j]) < height :
            sum+=1

print("\nsum of visible trees from all 4 sides : ",sum,"\n")

# we found 21 as expected with the test.txt file