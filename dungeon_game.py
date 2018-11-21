import os
import random
import time

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw the player in the grid
# move player unless move is invalid
# check for win/loss
# take input for movement
# clear the screen and redraw the grid


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
         ]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


def draw_map(player, player_icon="X"):
    print(" _" * 5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("{}".format(player_icon))
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def end_game():
    clear_screen()
    print("\n ** See you next time! ** \n")
    time.sleep(2.5)
    clear_screen()
    raise SystemExit()


def game_loop():
    clear_screen()
    monster, door, player = get_locations()
    playing = True
    top_message = "Welcome to the dungeon!"
    print(top_message)
    top_message = "\n"
    input("Press return/enter to start.")

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        if top_message:
            print(top_message)
        print("One of these squares holds the door out of here.")
        print("One of these squares is the home of a terrifying monster.")
        print("You must try to escape the dungeon!")
        print("Type {} to move your character.".format(", ".join(valid_moves)))
        print("Enter QUIT to quit.")
        try:
            move = input("> ").upper()
            if move.upper() not in ["LEFT", "RIGHT", "UP", "DOWN", "QUIT"]:
                raise ValueError
        except ValueError:
            top_message = ("\n ** That's not a valid move."
                           + "Please try again **"
                           )
            continue
        if move == 'QUIT':
            end_game()
        if move in valid_moves:
            player = move_player(player, move)
            top_message = "\n"

            if player == monster:
                clear_screen()
                draw_map(player, "M")
                print("\n ** Oh no! The monster got you!"
                      + "Better luck next time! **"
                      )
                playing = False

            if player == door:
                clear_screen()
                draw_map(player, "D")
                print("\n ** You escaped! Congratulations! **\n")
                playing = False

        else:
            top_message = "\n ** Walls are hard! Don't run into them!**"
    else:
        if input("Play again? [Y/n] ").lower() != "n":
            clear_screen()
            game_loop()
        else:
            end_game()


game_loop()
