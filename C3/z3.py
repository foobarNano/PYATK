from random import randint

points = [0,0]
#   [P1, P2/CPU]

def clearscreen():
    print('\n\n\n\n\n\n\n\n')

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
