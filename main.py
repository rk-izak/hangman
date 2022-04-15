import random


def find(word, charac):
    for i, ltr in enumerate(word):
        if ltr == charac:
            yield i



print("H A N G M A N")

alphabet = str('abcdefghijklmnopqrstuvwxyz')
alphabet_small = set(alphabet)
alphabet_capital = alphabet.upper()
alphabet_capital = set(alphabet_capital)

won_times = 0
lost_times = 0

while True:
    j = 0
    decision = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    word_list = ('python', 'java', 'swift', 'javascript')
    chosen = random.choice(word_list)
    chosen_list = list(chosen)
    answer = list('-' * len(chosen))
    guessed = set()

    if decision == 'play':
        print()
        while j < 8:
            print("".join(answer))
            letter = input("Input a letter: ")

            if (letter not in alphabet_small and len(list(letter)) == 1) or \
                    (letter in alphabet_capital and len(list(letter)) == 1):
                print('Please, enter a lowercase letter from the English alphabet.')
                print()
                continue
            elif len(list(letter)) != 1:
                print('Please, input a single letter.')
                print()
                continue
            elif letter in alphabet_small:

                if letter in chosen_list:
                    if letter in guessed:
                        print("You've already guessed this letter.")
                    else:
                        b = list(find(chosen, letter))
                        for n in range(len(b)):
                            answer[b[n]] = letter

                elif letter not in chosen_list:
                    if letter in guessed:
                        print("You've already guessed this letter.")
                    else:
                        print("That letter doesn't appear in the word.")
                        j += 1

                if answer == chosen_list:

                    print("You guessed the word " + "".join(answer) + "!")
                    print("You survived!")
                    won_times += 1
                    break
            guessed.add(letter)
            print()
        if answer != chosen_list:
            print("You lost!")
            lost_times += 1

    elif decision == 'results':
        print("You won: {} times.".format(won_times))
        print("You lost: {} times.".format(lost_times))


    elif decision == 'exit':
        break
