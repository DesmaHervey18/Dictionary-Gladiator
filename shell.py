import core
from time import sleep


def welcome():
    print('Greeting Gamer\'s', 'Welcome to The Beowulf Gladiator Game\n')
    print('...LOADING...')
    sleep(1)
    print('...LOADING...')
    sleep(1)
    print('...LOADING...')
    sleep(1)
    print('...LOADING...\n')
    while True:
        response = input(
            'Are you sure you would to play The Beowulf Gladiator Game???\n'
        ).strip().lower()
        if response == 'yes':
            print('Wait a moment, while we load.')
            break
    if response == 'no':
        exit()
    print('...LOADING...')
    sleep(1)
    print('...LOADING...')
    sleep(1)
    print('...LOADING...')
    sleep(1)
    print('...LOADING...')
    print('\nOK Let\'s get started.\n')
    while True:
        response = input('press [A] to continue\n').strip().lower()
        if response == 'a':
            print('...LOADING...')
            sleep(1)
            print('...LOADING...')
            sleep(1)
            print('...LOADING...')
            sleep(1)
            print('...LOADING...\n')
            print('****ON YOUR MARK****\n')
            print('**** GET SET****\n')
            print('*~*~*~B A T T L E~*~*~*\n')

            break


def gladiator(name_1, name_2):
    gladiator_one = core.new_gladiator(100, 0, 19, 33)
    gladiator_two = core.new_gladiator(100, 0, 20, 33)
    while True:
        print(name_1, gladiator_one['health'], 'hp', '!!!',
              gladiator_one['rage'], 'rage')
        print(name_2, gladiator_two['health'], 'hp', '!!!',
              gladiator_two['rage'], 'rage\n')
        while True:
            print('\nplayer one:\n {} your turn'.format(name_1))
            response = input(
                'Would you like to{}...???\n 1.[A]ttack, 2.[P]ass, 3.[Q]uit, 4.[H]eal'
            )
            if response == 'A':
                core.attack(gladiator_one, gladiator_two)
                print('gladiator_two health', gladiator_two['health'])
                break
            elif response == 'P':
                break
            elif response == 'Q':
                return
            elif response == 'H':
                core.heal(gladiator_one)
        if core.is_dead(gladiator_two):
            print('{}: YOU WIN!'.format(name_1))
            print('POOR TINK-TINK, YOU\'RE DEAD!!!!!')
            print('**~~~~GAME OVER~~~~**')
            break
        while True:
            print('\nplayer two:\n {} your turn'.format(name_2))
            response = input(
                'Would you like to...???\n 1.[A]ttack, 2.[P]ass, 3.[H]eal], 4.[Q]uit'
            )
            if response == 'A':
                core.attack(gladiator_two, gladiator_one)
                print('gladiator_one health', gladiator_one['health'])
                break
            elif response == 'P':
                break
            elif response == 'Q':
                return
            elif response == 'H':
                core.heal(gladiator_two)
        if core.is_dead(gladiator_one):
            print('{}: YOU WIN!'.format(name_2))
            print('POOR TINK-TINK, YOU\'RE DEAD!!!!!\n')
            print('**~~~~GAME OVER~~~~**\n')
            break


def main():
    welcome()
    name_1 = input('What is your name >>>')
    name_2 = input('What is your name player 2.')
    gladiator(name_1, name_2)


if __name__ == '__main__':
    main()
