# Hangman Game

import pyfiglet
import random


# print hangman func
def print_hangman():
    """
    Create hangman print ascii art list.
    :rtype: list
    """
    HANGMAN_FAILED_ASCII_ART_1 = 'x-------x'

    HANGMAN_FAILED_ASCII_ART_2 = 'x-------x\n' \
                                 '|\n' \
                                 '|\n' \
                                 '|\n' \
                                 '|\n' \
                                 '|\n'

    HANGMAN_FAILED_ASCII_ART_3 = 'x-------x\n' \
                                 '|       |\n' \
                                 '|       0\n' \
                                 '|\n' \
                                 '|\n' \
                                 '|\n'

    HANGMAN_FAILED_ASCII_ART_4 = 'x-------x\n' \
                                 '|       |\n' \
                                 '|       0\n' \
                                 '|       |\n' \
                                 '|\n' \
                                 '|\n'

    HANGMAN_FAILED_ASCII_ART_5 = 'x-------x\n' \
                                 '|       |\n' \
                                 '|       0\n' \
                                 '|      /|\ \n' \
                                 '|\n' \
                                 '|\n'

    HANGMAN_FAILED_ASCII_ART_6 = 'x-------x\n' \
                                 '|       |\n' \
                                 '|       0\n' \
                                 '|      /|\ \n' \
                                 '|      /\n' \
                                 '|\n'

    HANGMAN_FAILED_ASCII_ART_7 = 'x-------x\n' \
                                 '|       |\n' \
                                 '|       0\n' \
                                 '|      /|\ \n' \
                                 '|      / \ \n' \
                                 '|\n'

    # print hangman ascii art
    PRINT_HANGMAN = [HANGMAN_FAILED_ASCII_ART_1, HANGMAN_FAILED_ASCII_ART_2, HANGMAN_FAILED_ASCII_ART_3,
                     HANGMAN_FAILED_ASCII_ART_4, HANGMAN_FAILED_ASCII_ART_5,
                     HANGMAN_FAILED_ASCII_ART_6, HANGMAN_FAILED_ASCII_ART_7]

    return PRINT_HANGMAN


# is_alpha func
def is_alpha(dynamic_var):
    """
    iterate dynamic_var elements and return false if one of the elements in not alphabet
    :param dynamic_var: value argument to iterate
    :type dynamic_var: dynamic (str / list)
    :rtype: bool
    """
    for element in dynamic_var:
        if not element.isalpha():
            return False
    return True


# random_word func
def random_word():
    """
    Take file_path input contains words separate with ' ,' pattern.
    Choose random word from the file, and return it.
    :return the random guess word from file_path
    :rtype: str
    """
    while True:
        try:
            # YOU MUST HAVE txt file with words seperected by " ,"
            file_path = input('\nEnter words file path:\t')
            with open(r"%s" % file_path, "r") as input_file:
                words = input_file.read().split(', ')
            r_word = words[random.randint(0, len(words) - 1)]
            return r_word
        except FileNotFoundError:
            print('\nFile path not found, enter file path a valid file path.')


# chars validator func
def chars_validator(my_str=''):
    """
    create a validator list, each element is a nested list.
    Each nested list values are [char, char count in my_str, num of char guessed (0)]
    :param my_str: str argument
    :type my_str: str
    :return: validator chars list
    :rtype: list
    """
    non_duplicate_chars = list(dict.fromkeys(my_str))
    validator = [[letter, my_str.count(letter), 0] for letter in non_duplicate_chars]
    return validator


# print hide word func
def print_hide_word(hide_word_list):
    """
    iterate hide_word_list.
    when char is hidden show '_'
    when char is in hidden show char.
    :param hide_word_list:
    :return the combine str with hidden and un hidden chars.
    :rtype: str
    """
    hide_word = ''
    for element in hide_word_list:
        if element[1]:
            hide_word += '_ '
        else:
            hide_word += (element[0] + ' ')
    return hide_word


# main func
def main():
    # ascii banner
    ASCII_BANNER = pyfiglet.figlet_format("WELCOME TO HANGMAN ! ! !")
    # max tries num
    MAX_TRIES = 6
    # current tries num
    current_tries = 0
    # failed tries num
    failed_tries = 0
    # success tries num
    success_tries = 0
    # hangman ascii art list
    PRINT_HANGMAN = print_hangman()
    # store success guessed chars
    old_letters_guessed = []

    # print welcome ascii banner
    print('\n', ASCII_BANNER)

    # guess word, save the word length, and create hide word
    # taking file path input from the user and choose random word from the file words.
    guess_word = random_word()
    # save guess_word length
    guess_word_len = len(guess_word)
    # create chars list validator
    chars_list_validator = chars_validator(guess_word)
    # create hide_words, set hide all words default
    hide_words = [[letter, True] for letter in guess_word]
    print_hide_word(hide_words)
    # print good luck
    print('\nYour have %d tries, Good Luck!\n' % MAX_TRIES)
    # print hangman [0].
    print(PRINT_HANGMAN[0])

    # guess chars until MAX_TRIES or success
    while True:
        try:
            # taking input from the user, lower case the input
            guess_char = input('\nGuess a letter:\t').lower()
            if not is_alpha(guess_char):
                print('\nPls enter only letters')
                continue
            if len(guess_char) > 1:
                print('\nYou can only enter one letter at a time')
                continue

            # check if guess_char in guess_word
            if guess_char in guess_word:

                # validate char in validator list
                for i in range(len(chars_list_validator)):
                    if chars_list_validator[i][0] == guess_char:
                        # check if char appears in guess_word is equal to the specific num of char guesses
                        if chars_list_validator[i][1] == chars_list_validator[i][2]:
                            print('\nTry enter different chars then %s.' % ', '.join(old_letters_guessed))
                        else:
                            # add 1 to validator value of the specific guess_char
                            chars_list_validator[i][2] += 1
                            # add guess char to old_letters_guessed
                            if guess_char not in old_letters_guessed:
                                old_letters_guessed.append(guess_char)
                            # update success_tries
                            success_tries += 1
                            # un hide char in hide_words list
                            for element in hide_words:
                                if element[0] == guess_char and element[1]:
                                    element[1] = False
                                    break
                            print('\n', print_hide_word(hide_words))

                        # break loop if char found in validator list
                        break

            # if guess_char not in guess_word
            else:
                # update current tries
                current_tries += 1
                # update failed_tries
                failed_tries += 1
                # print hangman failed art with the failed_tries index
                print(
                    f'\n{PRINT_HANGMAN[failed_tries]}\nYou have {MAX_TRIES - failed_tries} tries left')
            # win check
            if success_tries == guess_word_len:
                # print you win the game in ascii art
                print(pyfiglet.figlet_format("YOU WIN THE GAME !"))
                break
            # failed check
            if current_tries == MAX_TRIES:
                # print better luck next time in ascii art
                print(pyfiglet.figlet_format("BETTER LUCK NEXT TIME : ("))
                break
        except ValueError:
            print('\nAn error has been occurred, pls enter a valid letter')


if __name__ == '__main__':
    main()
