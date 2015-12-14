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

while True:
    print("You are in cave", player_location)
    if (player_location == wumpus_location - 1 or player_location == wumpus_location + 1):
        print("I smell a Wumpus!")
    print("Which cave next?")
    player_input =  raw_input(">")
    if(not player_input.isdigit() or int(player_input) not in cave_numbers):
        print(player_input, "is not a cave!")
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Aargh! You got eatten by a wumpus!"
            break
