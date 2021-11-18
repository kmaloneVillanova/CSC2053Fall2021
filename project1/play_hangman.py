from hangman import Hangman

game = Hangman()
game.play()
print("Would you like to play again? yes or no")
y = input()
while y == 'yes':
    game.play()
    print("Would you like to play again? yes or no")
    y = input()