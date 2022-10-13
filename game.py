'''
Game modeul
'''
import random

SCISSOR = 1
PAPER = 2
ROCK = 3

# Define choice and mapper
dict_choice_mapper = {
    SCISSOR: 'Scissor',
    PAPER: 'Paper',
    ROCK: 'Rock'
}


def random_pick():
    '''
    Ranodmly pick a number of [1, 2, 3]

    Args:
        None

    Returns:
        choice: integer between 1 to 3.
    '''
    choice = random.randint(1, 3)
    return choice


def validate_user_choice(user_choice):
    '''
    Validate user choice. Only valid if user_choice is '1', '2', '3'.

    Args:
        user_choice: string, user input choice

    Returns:
        True if user choice is valid.
        False if user choice is invalid.
    '''

    if user_choice in ['1', '2', '3']:
        return True

    return False


def compare_choice(computer_choice, user_choice):
    '''
    Compare the computer choice and user choice, return which side wins.

    Args:
        computer_choice: int, computer choice.
        user_choice: int, user choice.
    Returns:
        int, 1 means computer win, 2 means user win,
        0 means no winner.
    '''
    computer_win = (computer_choice == SCISSOR and user_choice == PAPER) \
        or (computer_choice == ROCK and user_choice == SCISSOR) \
        or (computer_choice == PAPER and user_choice == ROCK)

    if computer_win:
        return 1

    user_win = (user_choice == SCISSOR and computer_choice == PAPER) \
        or (user_choice == ROCK and computer_choice == SCISSOR) \
        or (user_choice == PAPER and computer_choice == ROCK)

    if user_win:
        return 2

    return 0


def playloop():
    '''
    Looping for the game.
    '''
    message = '''
    Options
    1: Scissor
    2: Paper
    3: Rock
    Select your choice ('Q' to quit):
    '''

    computer_point = 0
    user_point = 0
    n_round = 0

    while True:
        computer_choice = random_pick()
        user_choice = input(message)
        if user_choice.upper() == 'Q':
            print('Bye.')
            return

        if not validate_user_choice(user_choice):
            print('Please select correct option [1, 2, 3].')
            continue

        user_choice = int(user_choice)
        n_round += 1

        res = compare_choice(computer_choice, user_choice)
        print()
        print(
            f'Computer choice: {dict_choice_mapper[computer_choice]}, \
            User choice: {dict_choice_mapper[user_choice]}')
        if res == 1:
            computer_point += 1
            print('Computer get one point.')
        elif res == 2:
            user_point += 1
            print('You get one point.')
        else:
            print('Tie.')

        print('-'*20)
        print(
            f'Round {n_round}. Points: Computer: {computer_point},\
                User: {user_point}')
        if computer_point == 5:
            print('Computer wins!')
            computer_point, user_point, n_round = 0, 0, 0
        elif user_point == 5:
            print('Congratulations! You Win!')
            computer_point, user_point, n_round = 0, 0, 0
        print('-'*20)


def main():
    '''
    Program entry.
    '''
    print("""
    Welcome to Scissor Paper Rock Game!
    Computer will randomly pick one of options of scissor, paper and rock.
    You are asked to choose your option of scissor, paper or rock.
    The first to get five points wins!
    """)

    playloop()


if __name__ == '__main__':
    main()
