import random
import sys

from capital_city_guesser import CapitalCityGuesser
from country_data import countries


def get_random_country() -> dict:
    max_country = len(countries) - 1
    random_country_int = random.randint(0, max_country)
    return countries[random_country_int]


def setup_game() -> CapitalCityGuesser:
    random_country = get_random_country()
    return CapitalCityGuesser(random_country)


def check_if_too_many_attempts(game: CapitalCityGuesser) -> None:
    if game.attemp_count == 3:
        print("Game over!!! - you've had too many attempts!\n")
        print(f"{game.capital} is the capital of {game.name}!")
        sys.exit()


def main() -> None:
    game = setup_game()
    print(f"\nWhat is the capital of {game.name}?\n")

    while game.guess_correct is False:
        check_if_too_many_attempts(game)
        print("\n\t", game.current_guess(), "\n\n")
        while True:
            guess = input("Enter your guess: ")
            if len(guess) <= game.max_input_length:
                game.attempt(guess)
                break
            print("Your guess has too many characters")
        game.check_if_fully_guessed()


if __name__ == "__main__":
    main()
