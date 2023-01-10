import re

from unidecode import unidecode


class CapitalCityGuesser:
    def __init__(self, country_data: dict) -> None:
        self.name = country_data["name"]
        self.capital = country_data["capital"]
        self.max_input_length = len(country_data["capital"])
        self.attemp_count = 0
        self.guess_correct = False

        self.__capital_normalised = unidecode(country_data["capital"])
        self.__capital_normalised_uppercase = self.__capital_normalised.upper()
        self.__capital_letter_list = list(self.__capital_normalised_uppercase)
        self.__guess_list = self.__generate_blank_guess_list()

    def current_guess(self) -> str:
        guess = ""
        for index in range(len(self.__guess_list)):
            guess += f"{self.__guess_list[index]} "
        return guess

    def attempt(self, guess: str) -> None:
        guess_upper = guess.upper()
        attempt_list = list(guess_upper)
        for letter_to_match in attempt_list:
            update_index_list = [
                index
                for index, letter in enumerate(self.__capital_letter_list)
                if letter == letter_to_match
            ]
            self.__update_guess(letter_to_match, update_index_list)
        self.attemp_count += 1

    def check_if_fully_guessed(self) -> None:
        if self.__capital_letter_list == self.__guess_list:
            self.guess_correct = True
            print(
                f"""You are correct! {self.capital} is the capital of {self.name}. \nYou guessed correctly in {self.attemp_count} attempts!
            """
            )

    def __generate_blank_guess_list(self) -> None:
        blank_guess = ""
        regex_pattern = re.compile("[A-Z]")
        for value in self.__capital_letter_list:
            if regex_pattern.fullmatch(value) is None:
                blank_guess += value
            else:
                blank_guess += "_"
        return list(blank_guess)

    def __update_guess(self, character: str, index_list: list) -> None:
        for index in index_list:
            self.__guess_list[index] = character
