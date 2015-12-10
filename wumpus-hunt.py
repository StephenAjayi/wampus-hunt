from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location =  choice(cave_numbers)
while wumpus_location == player_location:
    player_location = choice(cave_numbers)
