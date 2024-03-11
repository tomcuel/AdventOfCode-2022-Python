from collections import defaultdict
from heapq import heapify, heappop, heappush

#opening the file and reading the input
with open("input16.txt","r") as file:
    lines=file.read().strip().split("\n")

# default dict so that there is no problems of initialisation
# adj[node] is a list of the valves that the node is connected to
adj=defaultdict(list)
# flow[node] is the rate of the node
flow=defaultdict(int)
# nodes is a list of all the valves
nodes=[]
# node_idx is a dictionary that gives the line the valves appears in the input
# we hope that each node only appears once in the input, but it seems to be the case
node_idx={}

# parsing the input and filling the data structures
for i, line in enumerate(lines):
    parts=line.split(" ", 9) # so that the valves it lead to are in one groupe of the list : the last one 
    node=parts[1]
    nodes.append(node)
    node_idx[node]=i
    flow[node]=int(parts[4][5:-1])
    adj[node].extend(parts[-1].split(", "))


# function to get the pressure of the current state
# given which valves are open, we determine the pressure by summing the flow of the open valves
def get_pressure(state):
    total = 0
    for i in range(len(state)):
        if state[i]:
            total += flow[nodes[i]]
    return total


# the answer
ans = 0
# visited valves in the dfs
seen = set()
# pile is a stack of the pressure, the node we are at, the time remaining, and the state of the valves
pq = [(0, "AA", 30, (False,) * len(nodes))]

# TIME COMPLEXITY
# visiting 13 valves that have not 0 for flow
# might be to loog to be done in a reasonable time
# things need to be done to reduce the time complexity
total_states = 30 * 13 * (1 << 13)

# DFS algorithm
while len(pq) > 0:
    front = heappop(pq)
    pressure, node, time, state = front
    pressure = -pressure

    # if we've already visited this state, we don't need to visit it again
    if (pressure, node, time, state) in seen:
        continue
    seen.add((pressure, node, time, state))

    # we're stopping the search if we've reached the end of timing
    # we then need to consider another path
    if time == 0:
        ans = max(ans, pressure)
        print(f"Current answer: {ans}")
        continue

    idx = node_idx[node]

    # we need not to consider the pressure we will add to the current pressure
    pressure += get_pressure(state)

    # 1. open the valve
    # it takes 1 minute to open a valve, time --> time-1
    if flow[node] > 0 and not state[idx]:
        new_state = list(state)
        new_state[idx] = True
        new_state = tuple(new_state)
        heappush(pq, (-pressure, node, time - 1, new_state))

    # 2. move to a neighbor
    # it takes 1 minute to move to a neighbor, time --> time-1 
    for nbr in adj[node]:
        heappush(pq, (-pressure, nbr, time - 1, state))

    heappush(pq, (-pressure, node, time - 1, state))


# That's it
print("Answer:", ans)


# It does seems to go on forever, even if the answer might be correct, by seeing the trend of the answer that are printed