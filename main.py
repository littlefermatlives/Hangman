import random
from hangman_art import stages, logo
from hangman_words import word_list


# starting the game
print(logo)
is_game_end = False
lives = len(stages)  - 1

# choose a random word from the give list of words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
# print(chosen_word)



for i in range(word_length):
    display.append('_')


# guess = input("Guess your character -> ")
# if chosen_word.find(guess) != -1:
#     print("Found")
# else :
#     print("Not Found")
# cnt = 0
while not is_game_end:
    guess = input("Enter your character ->")
    pos = chosen_word.find(guess)
    if pos != -1 and display[pos] == '_':
        print("Your guess is correct!")
        print(stages[lives])
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print(''.join(display))
        check = False
        for i in range(word_length):
            if display[i] == '_':
                check = True
                break
        if check == False:
            is_game_end = True
            print("Game End, You Saved Your Hero!")

    else:
        print("Your Guess is Wrong. You lost a life")
        print(''.join(display))
        print(stages[lives])
        lives -= 1
        if lives < 0:
            is_game_end = True
            print("Game End, Your Hero is Dead!")
    # cnt += 1
    # if cnt >= 10:
    #     break

    
# guess = input("Enter your character ->")
# if chosen_word.find(guess) != -1:
#     for i in range(word_length):
#         if chosen_word[i] == guess:
#             display[i] = guess
#     print(''.join(display))
    



