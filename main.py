my_board = [["","","","","","",""],
            ["","x","x","","","",""],
            ["","x","","","","",""],
            ["","x","x","","x","",""],
            ["","x","","","","",""],
            ["","","","","","",""]]


def is_game_over(board):
    for row in board:
        cur_count = 1
        last_tile = ""
        for spot in row:
            if spot == last_tile and spot != "":
                cur_count += 1
            else:
                cur_count = 1
                last_tile = spot
            if cur_count == 4:
                return spot
    #Code above checks horizontal wins
    for row_num in range(3):
        for col_num in range(7):
            print(row_num,col_num)
            if board[row_num][col_num] == board[row_num+1][col_num] == board[row_num+2][col_num] == board[row_num+3][col_num] != "":
                return board[col_num][row_num]
    #Code above checks vertical wins

            
print(is_game_over(my_board))