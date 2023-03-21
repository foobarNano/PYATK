from random import randint

board = [0,0,0,0,0,0,0,0,0]
#   0 - Empty
#   1 - Player1
#   2 - Player2 / CPU

points = [0,0]
#   [P1, P2/CPU]

def clearscreen():
    print('\n\n\n\n\n\n\n\n')

def printboard():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
# 0 | 0 | 0
# --+---+--
# 0 | 0 | 0
# --+---+--
# 0 | 0 | 0

def checkboard():
    for i in range(0, 3):
        wcon1 = (board[3*i] == board[3*i+1] == board[3*i+2] != 0)
        wcon2 = (board[i] == board[i+3] == board[i+6] != 0)
        if wcon1 or wcon2: return board[i]
    wcon3 = (board[0] == board[4] == board[8] != 0) or (board[2] == board[4] == board[5] != 0)
    if wcon3: return board[4]
    if 0  in board: return 0
    return -1
#  1 - P1 won
#  2 - P2/CPU won
#  0 - Game not over
# -1 - Draw

while (True):
    clearscreen()
    print(  '----------------------------------------',
            'Rock Paper Scissors',
            '----------------------------------------', sep='\n')
    rcount = int(input("Number of rounds to play (0 to exit): "))
    if rcount == 0: break
    pvpmode = int(input("Number of players (1 or 2): ")) == 2
    p1name = input("Name for P1: ")
    p2name = input("Name for P2: ") if pvpmode else "CPU"

    for rnum in range(1, rcount+1):
        result = 0

        while True:
            clearscreen()
            print(p1name, ':\t', points[0], sep='')
            print(p2name, ':\t', points[1], sep='')
            print('ROUND ', rnum, '/', rcount, sep='')
            printboard()

            while True:
                choice = int(input('\n' + p1name + '\'s choice: '))
                if choice < 1 or choice > 9:
                    print('\tInvalid choice.')
                    continue
                if board[choice] != 0:
                    print('\tSpace taken.')
                    continue
                board[choice-1] = 1
                break
            result = checkboard()
            if result != 0: break

            if pvpmode:
                clearscreen()
                print(p1name, ':\t', points[0], sep='')
                print(p2name, ':\t', points[1], sep='')
                print('ROUND ', rnum, '/', rcount, sep='')
                printboard()

                while True:
                    choice = int(input('\n' + p2name + '\'s choice: '))
                    if choice < 1 or choice > 9:
                        print('\tInvalid choice.')
                        continue
                    if board[choice] != 0:
                        print('\tSpace taken.')
                        continue
                    board[choice-1] = 2
                    break
            else:
                avaible = list()
                for i in range(0, 9):
                    if board[i] == 0: avaible.append(i)
                choice = randint(0, len(avaible))
                board[choice] = 2
            result = checkboard()
            if(result!= 0): break
        
        if (result == 1):   points[0]+=1
        elif (result == 2): points[1]+=1
    
    board.clear()