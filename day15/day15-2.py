# opening the file 
with open("input15.txt","r") as file : 
    lines = file.read().strip().split("\n")

# parsing the data
# the index of the sensor is the same as the index of the nearest beacon corresponding to it 
sensors=[]
beacons=[]
for line in lines : 
    line=line.split(" ")

    xs=int((line[2].split(","))[0][2:])
    ys=int((line[3].split(":"))[0][2:])
    sensors.append((xs,ys))

    xb=int((line[8].split(","))[0][2:])
    yb=int((line[9].split(":"))[0][2:])
    beacons.append((xb,yb))

N=len(sensors)
distances=[]

# function to calculate the distance between two points of a matrix by using the path 
def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

# calculating the distances between the sensors and its nearest beacon
# index are the same for both sensors and beacons and distances
for i in range(N):
    distances.append(dist(sensors[i],beacons[i]))

print("sensor, beacon, distances : \n",sensors,beacons,distances,"\n")

# exclusion region for each sensor
# abs(s[i][0]-x)+abs(s[i][1]-y)< distances[i]
# we need to find the x and y that doesn't satisfy the condition, to find the distress beacon
# the point we're looking for is between 4 sensors "restricted area" 
# each sensor area is made of 4 lines 
# we're searching if one line in 1 tile away from another line
# then it needs to be the case for the 4 lines around a point 

# those are the side of the losange the restricted area are made of
pos_lines = []
neg_lines = []

for i, s in enumerate(sensors):
    d = distances[i]
    # the corner of the square of center (s[0],s[1]) are those 4 points
    # because d is the distance between from (s[0],s[1]) to the edge of the "restricted area"
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

print("negativ_affine_line : \n",neg_lines,"\n")
print("positiv_affine_line : \n",pos_lines,"\n")

# the area is twice the size of the distance between the sensor and its nearest beacon
# matching each line with the others ones 
# starting the sum from the next one to avoid to go through the same line

pos = None
neg = None

for i in range(2 * N):
    for j in range(i + 1, 2 * N):
        # going through postiv and negativ lines to check if they are 1 tile away from each other

        a, b = pos_lines[i], pos_lines[j]
        # condition to check if the line is 1 tile away from the other line
        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]
        # condition to check if the line is 1 tile away from the other line
        if abs(a - b) == 2:
            neg = min(a, b) + 1


# formumla that give the answer
x, y = (pos + neg) // 2, (neg - pos) // 2
ans = x * 4000000 + y
print("result : ",ans)