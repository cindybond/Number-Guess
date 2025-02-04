import random

def generate_random(lower, upper):
    random_num = random.randrange(lower, upper)
    print(random_num)
    return random_num

def guess_check(player_guess, random_num):
    if player_guess == random_num:
        print('CORRECT!')
        return True
    else:
        print('WRONG!')
        return False

def main():
    game_over = False
    print('Welcome to the Guessing Game!')
    print('-----------------------------')
    print('In this game, I will ask for 2 numbers from you, lower and upper. \n'
          'I will then randomly generate a number between the lower and upper. \n'
          'You will have to guess the number correctly! Think of it like hangman ...\n')     
 
    while True:
        while True:
            try:
                lower = int(input('Please enter lower number: '))
                break
            except ValueError:
                print('Oops! Please input an integer.')

        while True:
            try:
                upper = int(input('Please enter upper number: '))
                break
            except ValueError:
                print('Oops! Please input an integer.')  
    
        if lower >= upper:
            print('Please enter valid numbers. Lower has to be lower than Upper and not be the same number')
            continue

        random_num = generate_random(lower,upper)
        print('OK! I have a random number. Now you have to guess it...')
        game_over = False
        while not game_over:
                player_guess = int(input('Enter your guess: '))
                game_over = guess_check(player_guess, random_num)
            
        play_again = ""  # Initialize the play_again variable
        while True:
            if game_over:
                play_again = input('Do you want to play again? (Y/N): ').lower()
                if play_again == 'y':
                    print('Starting a new round...')
                    break  # Break to start a new round
                elif play_again == 'n':
                    print('Thanks for playing! See you again!')
                    return  # Exit the game
                else:
                    print('Invalid input. Please enter "Y" or "N"')
            
            

if __name__ == "__main__":
    main()