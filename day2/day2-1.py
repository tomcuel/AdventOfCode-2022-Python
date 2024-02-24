# Opening the file in read mode
with open('input2.txt', 'r') as file:
    # extracting the lines 
    lines = file.read().strip().split("\n")

# using a dictioinnary here is easier 
play_map = {"A": 0, "B": 1, "C": 2,
            "X": 0, "Y": 1, "Z": 2}
# A = rock, B = paper, C = scissors for opponent
# X = rock, Y = paper, Z = scissors for player
# the player win when : 
# - the opponent is rock (A) and the player is paper (Y), so the differnece is 1
# - the opponent is paper (B) and the player is scissors (Z), so the differnece is 1
# - the opponent is scissors (C) and the player is rockc(X), so the differnece is 1

score=0
for line in lines : 
    # each player is given the number corresponding to the letter in the dictionary   
    opponent, player = [play_map[i] for i in line.split()]

    # compare the difference between the player and the opponent to know who wins 

    if (player - opponent) % 3 == 1: # player wins
        score += 6

    elif player == opponent: # draw 
        score += 3

    score += player+1

print("le résultat est",score)

# it does print 15 for the test.txt exampke