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

# row that we are looking for 
Y = 2000000
# it will be the intervals that will contain the x (column) values 
# where we can't place the beacon 
# because we now thanks to the distances lists the map where there isn't any beacon for each sensor 
# because distance list is based on the nearest beacon for each sensor
intervals = []
for i, s in enumerate(sensors):
    # getting how far the sensor is from the Y row 
    # distances bteween the nearest beacon and the sensor
    # - the distance between the sensor_row and the Y row
    # give us the abciss delta
    dx=distances[i]-abs(s[1]-Y)

    # if the distance is negative, we can place the beacon
    if dx<=0:
        continue

    # insert the range of x values where we can't place the beacon
    intervals.append((s[0]-dx,s[0]+dx))

print("intervals :\n",intervals,"\n")

# sorting the intervals
# making the intersection of the intervals
# and then summing the length of the intervals still there 

# if there is a beacon on the Y row, then it's a place that is allowed
allowed_x = []
for bx, by in beacons:
    if by == Y:
        allowed_x.append(bx)

# going through the intervals
min_x_intervals = min([left for left, right in intervals])
max_x_intervals = max([right for left, right in intervals])

# summing the places where we can't place the beacon
sum=0

for x in range(min_x_intervals, max_x_intervals+1) : 
    # if the x is in the allowed_x list, then we can place the beacon
    # so we continue to the next x
    if x in allowed_x : 
        continue

    # if the x is not in the allowed_x list, then we can't place the beacon
    # we are then looking if the x is in the intervals
    # to have a bit less time of calcul we break to stop when we encounter the point 
    # we also remove the intervals that are not useful anymore to avoid to go through them again 
    for left, right in intervals : 
        if x >= right : 
            intervals.remove((left,right))

        if left <= x <= right : 
            sum+=1
            break

print("sum of the length of the intervals still there : ",sum)