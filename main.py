from sgfmill import sgf
with open("/home/user/Go_project/go_bot/sgf.sgf", "rb") as f:
    game = sgf.Sgf_game.from_bytes(f.read())

winner = game.get_winner()
print(winner)
board_size = game.get_size()
root_node = game.get_root()
b_player = root_node.get("PB")
w_player = root_node.get("PW")
print(w_player)

for node in game.get_main_sequence():
    print(node.get_move())