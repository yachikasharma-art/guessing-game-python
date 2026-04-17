import random 
def game():
    secret_number= random.randint(1,100)
    guesses=0
    print('hiii!, welcome to the guesseing game')
    print('I have picked number from 1 to 100')
    print("="*50)
    print("LET'S START")
    print("="*50+'\n')
    while True:
        guess= int(input('enter number you guessed:'))
        guesses+=1
        if guess<secret_number:
            print('-'*40)
            print('😊 higher number please!')
            print('-'*40+'\n')
        elif guess>secret_number:
            print('-'*40)
            print('😇 lower number please!')
            print('-'*40+'\n')
        else:
            print('-'*40)
            print('🎉yayyyyyy!!!🎉 you gussed  it right!!!')
            print(f'you got it with {guesses} guesses')
            print('-'*40+'\n')
            break
    print("-" * 40)
    play_again = input("Phir khelna hai? (y/n): ").lower()
    if play_again == "y":
        game()
    else:
        print("\nBye! Thanks for playing 👋")