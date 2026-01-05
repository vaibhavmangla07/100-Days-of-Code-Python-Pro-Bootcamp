# Maze layout as a dictionary
maze = {
    'start': {'east': 'hall'},
    'hall': {'west': 'start', 'south': 'trap', 'east': 'exit'},
    'trap': {'north': 'hall'},
    'exit': {}
}

# Starting point
position = 'start'

print("🧩 Welcome to Escape the Maze!")
print("You can move: north, south, east, or west.\n")

while True:
    print("You are in:", position)

    # Check if player reached the exit
    if position == 'exit':
        print("🎉 Congratulations! You escaped the maze!")
        break

    # Get user move
    move = input("Enter direction: ").lower()

    # Check if move is valid
    if move in maze[position]:
        position = maze[position][move]
    else:
        print("🚫 You can't go that way! Try a different direction.\n")
