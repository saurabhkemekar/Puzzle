import random

def replacment(list,n):
    if n in list:
        index = list.index(n)
        list[index] = 0
    return  list
def shifting(listx,n):
    listx1 = [listx[i] for i in range(n,9)]
    listx2 = [listx[i] for i in range(0,n)]
    return listx1+listx2
def solving_sudoku(sudoku):

    flag = 0
    row, col = first_empty(sudoku)
    #print('row {},col{}'.format(row,col))
    if row==-1 and col==-1:
        for rowx in sudoku:

            print(rowx)
        print("\n\n")
        return True

    else:
        option = [i for i in range(1, 10)]

        for op in option:
            if check_row(sudoku[row], op):
                if check_col(sudoku, col, op):
                    if check_3x3_box(sudoku, row, col, op):
                        flag =1
                        sudoku[row][col] = op
                        if  not solving_sudoku(sudoku):
                            flag =0

                            pass
    if flag ==0:
            sudoku[row][col] =0
            return False



def first_empty(sudoku):
    for i in range(len(sudoku)):
        if 0 in sudoku[i]:
            return i, sudoku[i].index(0)
    else:
        return -1,-1
def check_row(row, value):

    if value in row:
        return False
    else:
        return True
def check_col(sudoku, col_no, value):

    column = [row[col_no] for row in sudoku]
    if value in column:
        return False
    else:
        return True
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
row1 = [i for i in range(1,10)]

random.shuffle(row1)
row2 = shifting(row1,3)
row3 = shifting(row2,3)
row4 = shifting(row3,1)
row5 = shifting(row4,3)
row6 = shifting(row5,3)
row7 = shifting(row6,1)
row8 = shifting(row7,3)
row9 = shifting(row8,3)
sudoku = [row1,row2,row3,row4,row5,row6,row7,row8,row9]
level = input('DIFFCULTY LEVEL \n1) HARD\n2) MEDIUM\n3) EASY\n' )
if level == '1':
    remove_number = [7,8,9]
elif level =='2':
    remove_number = [5,6,7]
else:
    remove_number = [3,4,5]

for i in sudoku:
    num = random.choice(remove_number)
    count = 0
    while count<num:
        n = random.randint(1,9)
        i = replacment(i,n)
        count+=1
for row in sudoku:
    print(row)
print('\n\n')

#sudoku = [[8,6,0,0,0,9,7,0,0],[0,0,1,0,0,0,8,0,6],[7,0,0,0,4,0,0,1,0],[0,0,8,5,0,0,0,0,4],[0,0,4,8,0,7,2,0,0],[9,0,0,0,0,2,5,0,0],[0,1,0,0,8,0,0,0,7],[3,0,5,0,0,0,6,0,0],[0,0,7,9,0,0,0,3,2]]
solved_sudoku = solving_sudoku(sudoku)

########################################################################################

