import art
from word import get_word


class Game:
    def __init__(self):
        super().__init__()
        self.word = get_word()
        self.state = 0
        self.guessed_chars = set()
        self.answer = ["_"] * len(self.word)

    def print_answer(self):
        for char in self.answer:
            print("{} ".format(char), end="")
        print()

    def check_win(self):
        return False
        # if state < 10 and :

    def check_lose(self):
        return False
        # if state < 10 and :

    def check_ans(self, guess):
        # TODO check whole word
        correct = False
        for i,char in enumerate(self.word):
            if char == guess:
                self.answer[i] = char
                correct = True
        if not correct:
            self.state += 1

    def play(self):
        while True:
            # Win check
            if self.check_win():
                print("You win!")
                break
            if self.check_lose():
                print("You lose!")
                break

            # Print hangman art
            art.print_art(self.state)
            self.print_answer()

            guess = input("Write your guess: ")
            # input validation
            if not guess.isalpha() or len(guess) > 1:
                print("Please write a single letter")
                continue
            if guess in self.guessed_chars:
                print("You already chosen that letter")
                continue

            self.guessed_chars.add(guess)
            self.check_ans(guess)
