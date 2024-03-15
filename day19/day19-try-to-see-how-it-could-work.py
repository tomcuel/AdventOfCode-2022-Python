import dataclasses as dc
import functools as ft
import math

# opening the file 
with open("test.txt", "r") as file : 
    lines=file.read().strip().split("\n")   

# creating a class to store the blueprints of the input 
@dc.dataclass()
class Blueprint:
    index: int
    ore_ore: int
    clay_ore: int
    obs_ore: int
    obs_clay: int
    geode_ore: int
    geode_obs: int

    @ft.cached_property
    def max_ore(self) -> int:
        return max(self.ore_ore, self.clay_ore, self.obs_ore, self.geode_ore)
    

# getting the input and its datas
blueprints=[[] for _ in range(len(lines))]
for i, line in enumerate(lines):
    line=line.split(": ")
    
    part_index=line[0].split(" ")
    index_int=int(part_index[1])

    line=line[1].split(". ")

    part_ore=line[0].split(" ")
    ore_ore_int=int(part_ore[4])

    part_clay=line[1].split(" ")
    clay_ore_int=int(part_clay[4])

    part_obs=line[2].split(" ")
    obs_ore_int=int(part_obs[4])
    obs_clay_int=int(part_obs[7])

    part_geode=line[3].split(" ")
    geode_ore_int=int(part_geode[4])
    geode_obs_int=int(part_geode[7])

    blueprints[i]=Blueprint(index_int, ore_ore_int, clay_ore_int, obs_ore_int, obs_clay_int, geode_ore_int, geode_obs_int)


# printing the blueprints, just to see if the input is correctly stored
print("\nInput :")
for blueprint in blueprints:
    print(blueprint)
print("\n")


# give the state of the situation 

@dc.dataclass()
class state:
    time:int =dc.field(default=0)
    ore:int =dc.field(default=0)
    clay:int =dc.field(default=0)
    obs:int =dc.field(default=0)
    robot_ore:int =dc.field(default=1)
    robot_clay:int =dc.field(default=0)
    robot_obs:int =dc.field(default=0)
    robot_geode:int =dc.field(default=0)


test=blueprints[0]
state0=state()
print(state0)
while state0.time<24 :
    
    # ressources we gain from all the robots we have 
    for i in range(state0.robot_ore):
        state0.ore+=1
    for i in range(state0.robot_clay):
        state0.clay+=1
    for i in range(state0.robot_obs):
        state0.obs+=1


    if state0.ore >= blueprint.ore_ore and state0.obs >= blueprint.obs_ore :
        state0.ore-=blueprint.ore_ore
        state0.clay-=blueprint.clay_ore
        state0.obs-=blueprint.obs_ore
        state0.robot_geode+=1

    if state0.ore >= blueprint.ore_ore and state0.clay >= blueprint.clay_ore :
        state0.ore-=blueprint.ore_ore
        state0.clay-=blueprint.clay_ore
        state0.obs+=1

    if state0.ore >= blueprint.clay_ore :
        state0.ore-=blueprint.ore_ore
        state0.robot_clay+=1

    if state0.ore >= blueprint.ore_ore : 
        state0.ore-=blueprint.ore_ore
        state0.robot_ore+=1

    

    state0.time+=1

    print(state0)
       
       




