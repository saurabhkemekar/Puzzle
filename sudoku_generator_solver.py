import random


def generate_sudoku():
    row1 = [i for i in range(1, 10)]
    random.shuffle(row1)
    row2 = shifting(row1, 3)
    row3 = shifting(row2, 3)
    row4 = shifting(row3, 1)
    row5 = shifting(row4, 3)
    row6 = shifting(row5, 3)
    row7 = shifting(row6, 1)
    row8 = shifting(row7, 3)
    row9 = shifting(row8, 3)
    sudoku = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    level = input('DIFFCULTY LEVEL \n1) HARD\n2) MEDIUM\n3) EASY\n')
    if level == '1':
        remove_number = [7, 8, 9]
    elif level == '2':
        remove_number = [5, 6, 7]
    else:
        remove_number = [3, 4, 5]
    for i in sudoku:
        num = random.choice(remove_number)
        count = 0
        while count < num:
            n = random.randint(1, 9)
            i = replacment(i, n)
            count += 1
    return sudoku


def print_sudoku(sudoku):
    count_r = 0
    for rowx in sudoku:
        count_r += 1
        print('|', end="")
        count_c = 0
        for number in rowx:
            count_c += 1
            print(number, end=" ")
            if count_c == 3 or count_c == 6:
                print("|", end='')
        print("")
        if count_r == 3 or count_r == 6:
            print('____________________')
    print("\n\n")


# for shifhting the number by n digit to left
def shifting(listx, n):
    listx1 = [listx[i] for i in range(n, 9)]
    listx2 = [listx[i] for i in range(0, n)]
    return listx1 + listx2

    # for replacing digit


def replacment(list, n):
    if n in list:
        index = list.index(n)
        list[index] = 0
    return list


# for finding empty block
def first_empty(sudoku):
    for i in range(len(sudoku)):
        if 0 in sudoku[i]:
            return i, sudoku[i].index(0)
    else:
        return -1, -1


# this function find the solution of sudoku using backtrackking algorithm

def solving_sudoku(sudoku):
    flag = 0
    global atp
    row, col = first_empty(sudoku)
    # print('row {},col{}'.format(row,col))
    if row == -1 and col == -1:
        print_sudoku(sudoku)
        atp=1


    else:
        option = [i for i in range(1, 10)]

        for op in option:
            if check_row(sudoku[row], op):
                if check_col(sudoku, col, op):
                    if check_3x3_box(sudoku, row, col, op):
                        flag = 1
                        sudoku[row][col] = op
                        if not solving_sudoku(sudoku):
                            flag = 0

                            pass
    if flag == 0 and atp==0:
        sudoku[row][col] = 0
        return False


# checking the row
def check_row(row, value):
    if value in row:
        return False
    else:
        return True


# checking the columns
def check_col(sudoku, col_no, value):
    column = [row[col_no] for row in sudoku]
    if value in column:
        return False
    else:
        return True


# checkinh the 3*3 gird
def check_3x3_box(sudoku, row_no, col_no, value):
    a = row_no // 3
    b = col_no // 3
    flag = 0
    for r in range(a * 3, a * 3 + 3):
        for c in range(b * 3, b * 3 + 3):
            if sudoku[r][c] == value:
                flag = 1
                break

    if flag == 0:
        return True
    elif flag == 1:
        return False


##############################################################################################################################
attemp=1
global atp
atp=0
while attemp==1:
    sudoku = generate_sudoku()
    print_sudoku(sudoku)
    ans=int(input('Do you want solution?\n1) YES\n2) NO\n'))
    print('\n\n')

    if ans==1:
        solved_sudoku = solving_sudoku(sudoku)
        atp = 0
    attemp=int(input('Do you want to play again?\n1) YES\n2) NO\n'))
    print('\n')
