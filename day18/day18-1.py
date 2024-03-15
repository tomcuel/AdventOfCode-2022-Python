import numpy as np

# opening the file 
with open("input18.txt","r") as file : 
    lines= file.read().strip().split("\n")


# for line in lines : 
# line=x,y,z to give us the place of the cube on a map 

datas=set()
# going through the boxes
for line in lines : 
    x, y, z = map(int, line.split(","))
    datas.add((x, y, z))

print("datas : \n",datas,"\n")

answer=0
# going through the boxes 
for x,y,z in datas :
    covered=0

    pos=np.array((x,y,z))

    for coord in range(3) : 
        # dpos is the direction of the positive axis 
        # dneg is the direction of the negative axis
        # for each direction : x,y,z 

        dpos=np.array([0,0,0])
        dpos[coord]=1

        dneg=np.array([0,0,0])
        dneg[coord]=-1

        # looking if the boxes next to the current one are in datas, so they are covered
        covered+=tuple(pos+dpos) in datas
        covered+=tuple(pos+dneg) in datas

    # uncovered boxes are 6-covered boxes
    answer+=6-covered


print("answer : ",answer)  
  
# I found 64 for the test.txt file as expected