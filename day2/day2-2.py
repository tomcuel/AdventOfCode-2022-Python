# Opening the file in read mode
with open('input2.txt', 'r') as file:
    # extracting the lines 
    lines = file.read().strip().split("\n")

# we sill have A = rock, B = paper, C = scissors for opponent
# but X Y Z are now the result of the game
# we need to do it in reverse to get the result of the game
    
play_map = {"A": 0, "B": 1, "C": 2, 
            "X": -1, "Y": 0, "Z": 1}

score=0
for line in lines : 
    # opponent is given the number corresponding to the letter in the dictionary, while we get the result of the game we nned to happen  
    opponent, result = [play_map[i] for i in line.split()]

    score +=(result+1)*3

    # the player wins so he has 1 point more than the opponent, ie the result of a win
    # in a draw, both have the same score
    # the opponent wins so he has 1 point more than the player, we have -1 ie the result of a loss 
    score+=1+((result+opponent)%3)

print("le résultat est",score)

# we have the 12 score for the test.txt example as exepected 