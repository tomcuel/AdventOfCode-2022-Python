# opening the file 
with open("input19.txt", "r") as file : 
    lines=file.read().strip().split("\n")   

import typing
import math
import functools as ft
import dataclasses as dc

# creating a class to store the different blueprints of the input 
@dc.dataclass()
class Blueprint:
    index: int
    ore_ore: int
    clay_ore: int
    obs_ore: int
    obs_clay: int
    geode_ore: int
    geode_obs: int

    # give the maximum amount of ore that we need to make all type of transformations
    @ft.cached_property
    def max_ore(self) -> int:
        return max(self.ore_ore, self.clay_ore, self.obs_ore, self.geode_ore)


# give the state of the situation 
# updating the state of the situation with some functions 
@dc.dataclass(frozen=True, kw_only=True)
class State:
    time: int
    ore: int = dc.field(default=0)
    clay: int = dc.field(default=0)
    obs: int = dc.field(default=0)
    bot_ore: int = dc.field(default=1)
    bot_clay: int = dc.field(default=0)
    bot_obs: int = dc.field(default=0)
    bot_geode: int = dc.field(default=0)

    # ajust the time remaining and the ressources we get from the different robots we have on the board
    def step(self) -> typing.Self:
        return dc.replace(
            self,
            time=self.time - 1,
            ore=self.ore + self.bot_ore,
            clay=self.clay + self.bot_clay,
            obs=self.obs + self.bot_obs,
        )

    # function to give the maximum amount of ore that we can have, based on the current blueprint
    def ore_cap(self, bp: Blueprint) -> int:
        return bp.max_ore + (self.time - 1) * (bp.max_ore - self.bot_ore)

    def clay_cap(self, bp: Blueprint) -> int:
        return bp.obs_clay + (self.time - 1) * (bp.obs_clay - self.bot_clay)

    def obs_cap(self, bp: Blueprint) -> int:
        return bp.geode_obs + (self.time - 1) * (bp.geode_obs - self.bot_obs)

    # This method calculates and returns a new State object representing the capped resources based on the given blueprint
    # It ensures that the resources don't exceed their capacity.
    def cap(self, bp: Blueprint) -> typing.Self:

        #for each remaining round, we spend at most bp.max_ore ore and produce at least self.bot_ore ore
        # in other words, each round, we lose at most bp.max_ore-self.bot_ore

        return dc.replace(
            self,
            time=self.time,
            ore=min(self.ore, self.ore_cap(bp)),
            clay=min(self.clay, self.clay_cap(bp)),
            obs=min(self.obs, self.obs_cap(bp)),
        )

    # This method returns a generator of all possible next states based on the given blueprint
    # It considers actions and see if they are possible, and if they are, it returns the new state
    # it will make differents choice, explore differents type of actions that can be taken 
    def options(self, bp: Blueprint):
        # doing the next step
        yield (step := self.step()).cap(bp)

        # producing different robots, and making what it does on ressources 

        # producing ore_robot
        if (
            self.time >= 8
            and self.bot_ore < bp.max_ore
            and bp.ore_ore <= self.ore
            and self.ore < self.ore_cap(bp)
        ):
            yield dc.replace(
                step, ore=step.ore - bp.ore_ore, bot_ore=self.bot_ore + 1
            ).cap(bp)

        # producing clay_robot
        if (
            self.time >= 6
            and self.bot_clay < bp.obs_clay
            and bp.clay_ore <= self.ore
            and self.clay < self.clay_cap(bp)
        ):
            yield dc.replace(
                step, ore=step.ore - bp.clay_ore, bot_clay=self.bot_clay + 1
            ).cap(bp)

        # producing obs_robot
        if (
            self.time >= 4
            and self.bot_obs < bp.geode_obs
            and bp.obs_ore <= self.ore
            and bp.obs_clay <= self.clay
            and self.obs < self.obs_cap(bp)
        ):
            yield dc.replace(
                step,
                ore=step.ore - bp.obs_ore,
                clay=step.clay - bp.obs_clay,
                bot_obs=self.bot_obs + 1,
            ).cap(bp)

        # producing geode_robot
        # we want it before the other robots, because it's the most important one
        if self.time >= 2 and bp.geode_ore <= self.ore and bp.geode_obs <= self.obs:
            yield dc.replace(
                step,
                ore=step.ore - bp.geode_ore,
                obs=step.obs - bp.geode_obs,
                bot_geode=self.bot_geode + 1,
            ).cap(bp)


# parsing the input to get the blueprints
def parse(lines : str) -> Blueprint:
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

    return blueprints


# function to search the best blueprint to use, by using function that maxes parameters
def search(bp: Blueprint, total: int):
    @ft.cache
    def go(s: State) -> int:
        # it's finished 
        if s.time == 0:
            return 0
        # if we have only one round left, we don't have time to make another geode_robot
        if s.time == 1:
            return s.bot_geode
        # else we can make a geode_robot and we can make another one if we have enough resources, so we need to iterate over the different options
        if s.time == 2:
            return 2 * s.bot_geode + (s.ore >= bp.geode_ore and s.obs >= bp.geode_obs)
        return s.bot_geode + max(map(go, s.options(bp)))

    print("blueprints index :",bp.index, "for a total of", go(State(time=total)), "geode_robot")
    # run it to now what the state would be at the end
    return go(State(time=total))




# printing the blueprints, just to see if the input is correctly stored
blueprints=parse(lines)
print("\nInput :")
for blueprint in blueprints:
    print(blueprint)
print("\n")

# adding the quality of each blueprint to the total
# a quality of blueprint means that we're maxing the number of geode_robot that we can make with the blueprint
answer = sum(bp.index * search(bp, 24) for bp in parse(lines))

print("\nthe answer is :",answer,"\n")

# we found 33 as expected with test.txt