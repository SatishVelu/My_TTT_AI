from random import choice


player = ''
computer = ''

def drawBoard(board):
    # Prints out board
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def inputPlayerLetter():
    # Player chooses between X or O
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Player goes first if X, otherwise computer goes first
    if player == 'X':
        return 'player'
    else:
        return 'computer'

def playAgain():
    print('Do you want to play again? (y/n)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    if won_vertical(board,letter) or won_horizontal(board,letter) or won_diagonal(board,letter):
        return True
    return False
    
def won_vertical(board, letter):
    return ((board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter))

def won_horizontal(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter))

def won_diagonal(board, letter):
    return ((board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your move? (1-9)')
        move = input()
    return int(move)

def isBoardFull(board):
    for j in range(1, 10):
        if board[j] == ' ':
            return False
    return True

def evaluate(board):
    if won_horizontal(board, computer):
        return +10
    elif won_horizontal(board, player):
        return -10
    elif won_vertical(board, computer):
        return +10
    elif won_vertical(board, player):
        return -10
    elif won_diagonal(board, computer):
        return +10
    elif won_diagonal(board, player):
        return -10

    return 0


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if isBoardFull(board):
        return 0

    if isMax:
        maxBest = -1000
        for k in range(1, 10):
            if board[k] == ' ':
                board[k] = computer
                maxBest = max(maxBest, minimax(board, depth+1, not isMax))
                board[k] = ' '
        return maxBest
    else:
        minBest = 1000
        for l in range(1, 10):
            if board[l] == ' ':
                board[l] = player
                minBest = min(minBest, minimax(board, depth+1, not isMax))
                board[l] = ' '
        return minBest

def getComputerMove(board):
    bestVal = -1000
    bestMove = -1

    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = computer
            moveVal = minimax(board, 0, False)
            board[i] = ' '
            if moveVal > bestVal:
                bestMove = i
                bestVal = moveVal
    return bestMove

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player, computer = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn is 'player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board, player, move)

            if isWinner(board, player):
                drawBoard(board)
                print('You have won! :)')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('It is a tie! :|')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(board)
            makeMove(board, computer, move)

            if isWinner(board, computer):
                drawBoard(board)
                print('You have lost! :(')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('It is a tie! :|')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break