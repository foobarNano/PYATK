from random import randint

points = [0,0]
#   [P1, P2/CPU]

choices = {
    1 : 'ROCK',
    2 : 'PAPER',
    3 : 'SCISSORS'
}

def clearscreen():
    print('\n\n\n\n\n\n\n\n')

def evaluate(p1choice: int, p2choice: int) -> int:
    if p1choice == p2choice: return 0
    if p1choice == p2choice%3 + 1: return 1
    return 2

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
        clearscreen()
        print(p1name, ':\t', points[0], sep='')
        print(p2name, ':\t', points[1], sep='')
        print('ROUND ', rnum, '/', rcount, sep='')

        p1choice = int(input('\n' + p1name + '\'s choice: '))
        p2choice = int()

        if pvpmode:
            clearscreen()
            print(p1name, ':\t', points[0], sep='')
            print(p2name, ':\t', points[1], sep='')
            print('ROUND ', rnum, '/', rcount, sep='')

            p2choice = int(input('\n' + p2name + '\'s choice: '))
        else:
            p2choice = randint(1, 3)

        clearscreen()
        print(choices[p1choice], ' VS ', choices[p2choice], sep='')
        result = evaluate(p1choice, p2choice)
        if result == 1:
            print(p1name, 'wins!')
            points[0] += 1
        elif result == 2:
            print(p2name, 'wins!')
            points[1] += 1
        else:
            print('Draw!')

        input('\n[PRESS ENTER TO CONTINUE]')

    clearscreen()
    print('Final score:', points[0], 'to', points[1])
    
    if points[0] > points[1]:   print('The winner is ', p1name, '!', sep='')
    elif points[1] > points[0]: print('The winner is ', p2name, '!', sep='')
    else:                       print('It\'s a draw!')

    input('\n[PRESS ENTER TO CONTINUE]')
