import random
from country_data import countries
from capital_city_guesser import CapitalCityGuesser


def get_random_country() -> dict:
    max_country = len(countries) - 1
    random_country_int = random.randint(0, max_country)
    return countries[random_country_int]


def main():
    random_country_dict = get_random_country()

    game = CapitalCityGuesser(random_country_dict)
    print(game.current_guess())
    game.attempt("abcdefghijklmnopqrstuvwxyz")
    print(game.current_guess())
    game.check_if_fully_guessed()


if __name__ == "__main__":
    main()
