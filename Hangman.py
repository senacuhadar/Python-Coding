player=input("Name: ")
print(f'Hello {player} time to play Hangman!')
findword="Adventure"
heart=10
totalword=['-' for j in findword]
print(''.join(totalword))
while heart > 0: 
            guess=input("Guess a letter: ").lower()
            if guess in findword.lower():
                for i in range(len(findword)):
                    if guess==findword[i].lower():
                        totalword[i]=guess
                print(' '.join(totalword)) 
                if ''.join(totalword)==findword.lower():
                        print('You won!!!')
                        break
            else: 
                print('Wrong!')
                heart -= 1 
                print(f'You have {heart} left.')

if heart == 0:
    print('You died!')
       
