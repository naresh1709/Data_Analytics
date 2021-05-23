import random
from secret_words import word_list
import json
import score_board


def get_secret_word():
    word = random.choice(word_list)
    return word.lower()


def play_hanman(word):
    allowed_errors = 5
    guesses = []
    done = False
    player_name = input("Please enter your name: ")
    player_score = score_board.get_player_score(player_name)
    print(player_name," Score :" ,player_score)
    while not done:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("-", end=" ")
        print("")

        guess = input(f"Allowed Error Left {allowed_errors},Guess your Letter : ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -= 1;
            if allowed_errors == 0:
                break
        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False
    if done:
        player_score += 10
        print("hurray You found the word!,It was ", word)
        print("Score obtained in this round is : ", 10)
    else:
        print("The Game is over! the word was ", word)
        print("Score obtained in this round is : ", 0)

    print("Your updated score is : ", player_score)
    score_board.update_player_score(player_name, player_score)
    score_board.update_top_10_player_list(player_name, player_score)


if __name__ == "__main__":
    word = get_secret_word()
    play_hanman(word)
    while input("Play Again? (Y/N) ").lower() == "y":
        word = get_secret_word()
        play_hanman(word)

    score_board.print_top_10_players()
    score_board.print_all_players_scores()
