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

directions = [[0,1],[0,-1],[1,0],[-1,0]]

score=0
# checking if the tree is visible from all 4 sides
for i in range(n) :
    for j in range(m) :
        height=datas[i][j] # height of tree at i,j
        temp=1

        # different conditons to check how many trees are visible from all 4 sides
        for di,dj in directions:
            # we go to the next tree in the direction of the current direction
            ii,jj=i+di,j+dj
            dist=0
            # loop to check if the tree is visible from the current direction
            while 0<=ii<n and 0<=jj<m and datas[ii][jj]<height:
                ii+=di
                jj+=dj
                dist+=1
                # if that will not be the case for the next one, we also add one, because this big tree will be visible from this direction
                if (0<=ii<n and 0<=jj<m) and datas[ii][jj]>=height:
                    dist+=1
            
            # we multiply the distance by the number of trees we can see from the each direction
            temp=temp*dist

        # we take the maximum distance from all 4 directions to be able to see the maximum number of trees
        score=max(score,temp)
        

print("\nsum of visible trees from all 4 sides : ",score,"\n")

# we found 8 as expected with the test.txt file