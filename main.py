import random
import sys

from capital_city_guesser import CapitalCityGuesser
from country_data import countries


def get_random_country() -> dict:
    max_country = len(countries) - 1
    random_country_int = random.randint(0, max_country)
    return countries[random_country_int]


def setup_game():
    random_country = get_random_country()
    return CapitalCityGuesser(random_country)


def check_if_too_many_attempts(game: CapitalCityGuesser):
    if game.attemp_count == 3:
        print("Game over!!! - you've had too many attempts!\n")
        print(f"{game.capital} is the capital of {game.name}!")
        sys.exit()


def main():
    game = setup_game()
    print(f"\nWhat is the capital of {game.name}?\n")

    while game.guess_correct is False:
        check_if_too_many_attempts(game)
        print("\t", game.current_guess(), "\n")
        guess = input("Enter your guess: ")
        game.attempt(guess)
        print("\n\t", game.current_guess(), "\n")
        game.check_if_fully_guessed()


if __name__ == "__main__":
    main()
