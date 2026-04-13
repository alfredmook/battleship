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
    print(" 0 1 2 3 4 5 6 7 8 9")
    for i,row in enumerate(grid):
        print(str(i)+" ".join(row))


player_ship_grid, player_attack_grid, computer_ship_grid, computer_attack_grid = initialize_grid()

player_ship_grid = place_ships(player_ship_grid)
computer_ship_grid = place_ships(computer_ship_grid)

 #PLAYER
turns = 30
def attack(put_x,put_y,opponent_ship_grid,self_attack_grid):
    cell = opponent_ship_grid[put_y][put_x]
    if cell != "~":
        print("Hit ship", cell)
        opponent_ship_grid[put_y][put_x] = "X"
        self_attack_grid[put_y][put_x] = cell
        return True
    else:
        print("MISS")
        opponent_ship_grid[put_y][put_x] = "O"
        self_attack_grid[put_y][put_x] = "#"
        return False
player_ship_status = 9
computer_ship_status = 9
#Total cells ships B,C and D have god forgive me
#Alfred please make this better danke schoen
win = False
for i in range(turns):
    print("Player's turn:")
    print("Ship grid: ")
    #display_grid(computer_ship_grid)
    display_grid(player_ship_grid)
    success = True
    while success:
        print("Attack grid: ")
        display_grid(player_attack_grid)
        while True:
            player_put_x, player_put_y = input("Input target coordinates in the format x,y: ").split(",")
            if not (player_put_x.isdigit() and player_put_y.isdigit()):
                print("Bro ts not valid frfr")
            else:
                player_put_x = int(player_put_x)
                player_put_y = int(player_put_y)
                if 0 <= player_put_x <= 9 and 0 <= player_put_y <= 9:
                    if player_attack_grid[player_put_y][player_put_x] != "~":
                        print("Cell was already selected before brodie select again")
                    else:
                        break #All checks passed can exit
        success = attack(player_put_x,player_put_y,computer_ship_grid,player_attack_grid)
        if success:
            computer_ship_status -= 1
            if computer_ship_status==0:
                win = True
                break
            print("Player gets to go again")
    if win:
        break
    print("CPU's turn:")
    while True:
        computer_put_x, computer_put_y = random.randint(0, 9), random.randint(0, 9)
        if computer_attack_grid[computer_put_y][computer_put_x] == "~":
            break
    if attack(computer_put_x,computer_put_y,player_ship_grid,computer_attack_grid):
        player_ship_status -= 1
    if player_ship_status == 0:
        break
if win:
    print("Yay you win you sunk all them ships")
else:
    print("Boo you lost")


