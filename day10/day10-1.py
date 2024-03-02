# opening the file 
with open("input10.txt", "r") as file : 
    # splitting the file into lines
    lines=file.read().strip().split("\n")

# printing the lines to see the data
print(lines)

# number of cycle being done 
cycle=0
# value of X
X=1
# we will add X*cycle at cycle =20, 60, 100, …
strength_signal=0

# list of the cycle we need to take X value 
cycle_list=[20,60,100,140,180,220]


# looping through the lines
for line in lines :
    # checking if this is this first type of command
    if line=="noop" :  
        cycle+=1
        # if the cycle is in the list of the cycle we need to take X value
        if cycle in cycle_list :
            print("cycle",cycle,"\n")
            print("X",X,"\n")
            strength_signal+=X*cycle

    # looking at the second type of command
    else : 
        # splitting the line to separate the command and the value
        line=line.split(" ")
        # looking at the command, if it really is "addx"
        assert line[0]=="addx"
        # the number of cycle is increased by 2 each time 
        # first add
        cycle+=1
        if cycle in cycle_list :
            print("cycle",cycle,"\n")
            print("X",X,"\n")
            strength_signal+=X*cycle
        # second add 
        cycle+=1
        if cycle in cycle_list :
            print("cycle",cycle,"\n")
            print("X",X,"\n")
            strength_signal+=X*cycle
        # taking the value of the command
        value=int(line[1])
        X+=value

# printing the strength signal
print("The strength signal is", strength_signal,"\n")

# we fin 13140 as expected with the file test2.txt