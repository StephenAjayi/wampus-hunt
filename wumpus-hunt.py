from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location =  choice(cave_numbers)
while wumpus_location == player_location:
    player_location = choice(cave_numbers)

print("Welcome to Wumpus Hunt")
print("You can see %d caves" % len(cave_numbers))
print("To play, just type a number")
print("of the cave you wish to enter next")
