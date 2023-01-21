board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def main():

    printBoard(board)

    solveBoard(board)

    print("------------------------------------------------")

    printBoard(board)



def printBoard(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")    

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
    return None

def solveBoard(board):

    empty = findEmpty(board)

    if empty == None:
        return True
    else:
       row,col = empty



    for i in range(1,10):
        if validNumber(board,i,row,col):
            board[row][col] = i

            validSolution = solveBoard(board)

            if validSolution:
                return True
            else:
                board[row][col] = 0

    return False

# def solveBoard(board):
#     find = findEmpty(board)
#     if not find:
#         return True
#     else:
#         row, col = find



#     for i in range(1,10):
#         if validNumber(board, i, row, col):
#             board[row][col] = i

#             if solveBoard(board):
#                 return True

#             board[row][col] = 0

#     return False


def validNumber(board,num,row,col):

    #column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    #row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    boxRow = row // 3
    boxCol = col // 3
    
    for i in range(boxRow*3,(boxRow*3)+3):
        for j in range(boxCol*3,(boxCol*3)+3):
            if board[i][j] == num and (i != row or j != col):
                return False

    return True

if __name__ == "__main__":
    main()