__author__ = 'kristo'

from random import randint
import json


class FlashCard():

    def __init__(self, question, answer):
        #ToDo
        raise NotImplementedError

    @property
    def get_question(self):
        #ToDo
        raise NotImplementedError

    @property
    def get_answer(self):
        #ToDo
        raise NotImplementedError

    @property
    def get_representation(self):
        #ToDo
        raise NotImplementedError


class DeckOfFlashCards():

    _cards = []

    def __init__(self, dictionary=None):
        if dictionary is not None:
            self._load_deck_from_json(dictionary)
        else:
            print("Creating new deck..")
            self.deck_name = input("Give a name to deck: ")
            while True:
                response = input("Create next card? (y/n)")
                if response == "n":
                    if len(self._cards) > 1:
                        break
                    else:
                        print("Not enough cards! Please enter at least two cards.")
                elif response == "y":
                    self._create_card()
                else:
                    print("Invalid input!")
                    continue
            while True:
                response = input("Save Deck? (y/n)")
                if response == "y":
                    self.save_deck()
                    break
                elif response == "n":
                    break
                else:
                    continue

    def get_random_card(self):
        """:returns A random card from self._cards."""
        #ToDo
        raise NotImplementedError

    def _load_deck_from_json(self, json_obj):
        """Fills up self._cards with FlashCard objects.
         FlashCard constructor parameters read from json file."""
        #ToDo
        raise NotImplementedError

    def _create_card(self):
        """Asks user for question and answer. These are used to create an instance of FlashCard and this is in turn
        appended to self._cards."""
        #ToDo
        raise NotImplementedError

    def save_deck(self):
        """All card representations are added together into a dictionary. This is in turn written to a file."""
        data = {}
        for card in self._cards:
            #ToDo
            raise NotImplementedError
        json.dump(data, open(self.deck_name, "w"),  sort_keys=True, indent=4, separators=(',', ': '))


class FlashCardExercise():

    current_card = None

    def __init__(self):
        self.deck = self._prompt_for_deck()

    def start(self):
        while True:
            self._give_instructions_card()
            answer = input("What do you want to do next?")
            if answer == "n":
                self._ask_question()
                input("Press enter for answer..")
                self._give_answer()
            elif answer == "q":
                break

    def _prompt_for_deck(self):
        """Prompts user for a deck, which either needs to be created or loaded.
        :returns An instance of DeckOfFlashCards.
        """
        while True:
            self._give_instructions_deck()
            response = input()
            if response == "-n":
                #ToDo
                raise NotImplementedError
            elif response == "-l":
                return self._load_deck()
            else:
                print("Invalid Input")
                continue

    def _create_new_deck(self):
        """Creates a new DeckOfFlashCards."""
        #ToDo
        raise NotImplementedError

    @staticmethod
    def _load_deck():
        """A deck is loaded from json.
        :returns An instance of DeckOfFlashCards
        """
        while True:
            file_name = input("Please enter name of file with deck data: ")
            #ToDo
            raise NotImplementedError

    def _ask_question(self):
        #ToDo
        raise NotImplementedError

    def _give_answer(self):
        #ToDo
        raise NotImplementedError

    @staticmethod
    def _give_instructions_card():
        print("n for next card \nq quit.")

    @staticmethod
    def _give_instructions_deck():
        print("-n create new deck, -l load existing deck.")

if __name__ == "__main__":
    game = FlashCardExercise()
    game.start()