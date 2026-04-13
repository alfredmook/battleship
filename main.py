import random

def create_grid():
    """
    Creates a 10x10 grid

    Returns:
        A 10x10 grid
    """
    grid = []
    for row in range(10):
        templist = []
        for col in range(10):
            templist.append("~")
        grid.append(templist)
    return grid

def initialize_grid():
    """
    Creates a 10x10 grid for player ships, player attacks,computer ships, computer attacks

    Returns:
        The 4 grids
    """
    player_ship_grid = create_grid()
    player_attack_grid = create_grid()
    computer_ship_grid = create_grid()
    computer_attack_grid = create_grid()

    return player_ship_grid, player_attack_grid, computer_ship_grid, computer_attack_grid
    

def place_ships(grid):
    """
    Places ships on the grid
    
    Args:
        grid: The ship grid (player_ship_grid or computer_ship_grid)
    
    Returns:
        grid: The grid with ships placed on it
    """
    Battleship = (4,"B")
    Cruiser = (3,"C")
    Destroyer = (2,"D")
    ships = [Battleship, Cruiser, Destroyer] 
    
    valid_placement = False
    for ship in ships:
        valid_placement = False
        while not valid_placement:
            valid_placement = True
            orientation = random.randint(0,1) # 0 for horizontal, 1 for vertical
            x = random.randint(0,9)
            y = random.randint(0,9)
            if (x + ship[0] > 9 and orientation == 0) or (y + ship[0] > 9 and orientation == 1):
                valid_placement = False
                continue
            for i in range(ship[0]):
                if orientation == 0:
                    valid_placement = grid[y][x+i] == "~"
                else:
                    valid_placement = grid[y+i][x] == "~"
                if not valid_placement:
                    break

            if not valid_placement:
                continue
            
            for i in range(ship[0]):
                if orientation == 0:
                    grid[y][x+i] = ship[1]
                else:
                    grid[y+i][x] = ship[1]
    
    return grid

def display_grid(grid):
    for row in grid:
        print(" ".join(row))


player_ship_grid, player_attack_grid, computer_ship_grid, computer_attack_grid = initialize_grid()

print(place_ships(player_ship_grid))
print(place_ships(computer_ship_grid))

 #PLAYER
turns = 30

for i in range(turns):
    player_put_x, player_put_y = input("Input target coordinates in the format x, y: ").split(", ")
    if player_put_x.isdigit() and player_put_y.isdigit():
        pass
    player_put_x = int(player_put_x)
    player_put_y = int(player_put_y)


turns = turns - 1



if turns == 0 and ____:
    pass
#COMPUTER


computer_put_x, comptuter_put_y = random.randint(0, 9), random.randint(0, 9)



