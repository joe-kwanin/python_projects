# write your code here

def check_cell(values):
    if values.replace(" ", "").isnumeric():
        return True
    else:
        print("You should enter numbers!")
        return False


def check_digits(values):
    if 4 > int(values) > 0:
        return True


def new_cell_value(x, y):
    i = int(y) + 2
    j = int(x) - 1
    select_index = (j * 3 + i) - 3
    while default_cells[select_index] == "_":
        default_cells[select_index] = "X"
        nfirst_row = " ".join(default_cells[0:3]).replace("_", " ")
        nsecond_row = " ".join(default_cells[3:6]).replace("_", " ")
        nthird_row = " ".join(default_cells[6:9]).replace("_", " ")
        print("---------")
        print("| " + nfirst_row + " |")
        print("| " + nsecond_row + " |")
        print("| " + nthird_row + " |")
        print("---------")
        check_winner(default_cells)
    else:
        print("This cell is occupied! Choose another one!")
        n_cordinate_val = input("Enter the coordinates: ")
        looping(n_cordinate_val)
        return True

def new_o_cell_value(x, y):
    i = int(y) + 2
    j = int(x) - 1
    select_index = (j * 3 + i) - 3
    while default_cells[select_index] == "_":
        default_cells[select_index] = "O"
        nfirst_row = " ".join(default_cells[0:3]).replace("_", " ")
        nsecond_row = " ".join(default_cells[3:6]).replace("_", " ")
        nthird_row = " ".join(default_cells[6:9]).replace("_", " ")
        print("---------")
        print("| " + nfirst_row + " |")
        print("| " + nsecond_row + " |")
        print("| " + nthird_row + " |")
        print("---------")
        check_winner(default_cells)
    else:
        print("This cell is occupied! Choose another one!")
        n_cordinate_val = input("Enter the coordinates: ")
        looping(n_cordinate_val)
        return True


def looping(entered_cell):
    while check_cell(entered_cell):
        row1, col2 = entered_cell.split()
        looping2(row1, col2)
        break
    else:
        entered_cell = input("Enter the coordinates: ")
        looping(entered_cell)


def looping2(x, y):
    x_num = 0
    o_num = 0
    num_ = 0
    for select in default_cells:
        if select == "X":
            x_num += 1
        elif select == "O":
            o_num += 1
        elif select == "_":
            num_ += 1
    while check_digits(x) and check_digits(y):
        if abs(x_num - o_num) > 0 or o_num == 0 and x_num != 0:
            new_o_cell_value(x, y)
        else:
            new_cell_value(x, y)
    else:
        print("Coordinates should be from 1 to 3!")
        entered_cell = input("Enter the coordinates: ")
        looping(entered_cell)


def check_winner(new_cells):
    first_row = " ".join(new_cells[0:3])
    second_row = " ".join(new_cells[3:6])
    third_row = " ".join(new_cells[6:9])
    first_col = " ".join(new_cells[0:8:3])
    second_col = " ".join(new_cells[1::3])
    third_col = " ".join(new_cells[2::3])
    first_dia = " ".join(new_cells[::4])
    second_dia = " ".join(new_cells[2:8:2])
    x_col_win = first_col == "X X X" or second_col == "X X X" or third_col == "X X X"
    o_col_win = first_col == "O O O" or second_col == "O O O" or third_col == "O O O"
    x_dia_win = first_dia == "X X X" or second_dia == "X X X"
    o_dia_win = first_dia == "O O O" or second_dia == "O O O"
    x_row_win = first_row == "X X X" or second_row == "X X X" or third_row == "X X X"
    o_row_win = first_row == "O O O" or second_row == "O O O" or third_row == "O O O"
    if x_col_win and o_col_win:
        print("Impossible")
    elif x_row_win:
        print("X wins")
        exit()
    elif o_row_win:
        print("O wins")
        exit()
    elif o_col_win:
        print("O wins")
        exit()
    elif x_col_win:
        print("X wins")
        exit()
    elif x_dia_win:
        print("X wins")
        exit()
    elif o_dia_win:
        print("O wins")
        exit()

    x_num = 0
    o_num = 0
    num_ = 0
    for select in new_cells:
        if select == "X":
            x_num += 1
        elif select == "O":
            o_num += 1
        elif select == "_":
            num_ += 1

    if x_num == o_num and num_ > 0:
        cordinates_val = input("Enter the coordinates: ")
        looping(cordinates_val)

    elif num_ == 0 and x_num > o_num or o_num > x_num:
        print("Draw")
        exit()
    else:
        cordinates_val = input("Enter the coordinates: ")
        looping(cordinates_val)


print("---------")
print("|       |")
print("|       |")
print("|       |")
print("---------")
default_cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
cordinate_val = input("Enter the coordinates: ")
while check_cell(cordinate_val.replace(" ", "")):
    row, col = cordinate_val.split()
    while check_digits(row) and check_digits(col):
        while new_cell_value(row, col):
            row, col = input("Enter the coordinates: ").split()
            new_cell_value(row, col)
            break
        else:
            new_cell_value(row, col)
        break
    else:
        print("Coordinates should be from 1 to 3!")
        entered_new_cell = input("Enter the coordinates: ")
        looping(entered_new_cell)
    break
else:
    entered_new2_cell = input("Enter the coordinates: ")
    looping(entered_new2_cell)

