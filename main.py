__author__ = 'kristo'

import random
import json


class FlashCard():

    def __init__(self, question, answer):
        self._question = question
        self._answer = answer

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def representation(self):
        return {self._question: self._answer}.items()


class DeckOfFlashCards():

    _cards = []

    def __init__(self, json_obj=None):
        if json_obj is not None:
            self._load_deck_from_json(json_obj)
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
        return self._cards[random.randint(0, len(self._cards)-1)]

    def _load_deck_from_json(self, json_obj):
        for key in json_obj.keys():
                self._cards.append(FlashCard(key, json_obj[key]))
        print("Finished loading deck.")

    def _create_card(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        self._cards.append(FlashCard(question, answer))

    def save_deck(self):
        data = {}
        for card in self._cards:
            data = dict(data.items() | card.representation)
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
        while True:
            self._give_instructions_deck()
            response = input("")
            if response == "-n":
                return DeckOfFlashCards()
            elif response == "-l":
                return self._load_deck()
            else:
                print("Invalid Input")
                continue

    def _create_new_deck(self):
        self.deck = DeckOfFlashCards()

    @staticmethod
    def _load_deck():
        while True:
            file_name = input("Please enter name of file with deck data: ")
            try:
                json_obj = json.load(open(file_name, "r"))
                return DeckOfFlashCards(json_obj=json_obj)
            except FileNotFoundError:
                print("Invalid file name.")
                continue

    def _ask_question(self):
        self.current_card = self.deck.get_random_card()
        print("Question: ")
        print(self.current_card.question)

    def _give_answer(self):
        print("Answer: ")
        print(self.current_card.answer)

    @staticmethod
    def _give_instructions_card():
        print("n for next card \nq quit.")

    @staticmethod
    def _give_instructions_deck():
        print("-n create new deck, -l load existing deck.")

if __name__ == "__main__":
    game = FlashCardExercise()
    game.start()