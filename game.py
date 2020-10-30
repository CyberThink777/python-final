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
        if self.state < 10 and self.word == ''.join(self.answer):
            return True
        return False

    def check_lose(self):
        if not self.state < 10:
            return True
        return False

    def check_ans(self, guess):
        correct = False
        if len(guess) > 1:
            if self.word == guess:
                correct = True
                for i, char in enumerate(self.word):
                    self.answer[i] = char
        else:
            for i, char in enumerate(self.word):
                if char == guess:
                    self.answer[i] = char
                    correct = True
        if not correct:
            self.state += 1

    def play(self):
        while True:
            # Print hangman art
            print()
            art.print_art(self.state)
            self.print_answer()
            # Win check
            if self.check_win():
                print("You win!")
                break
            if self.check_lose():
                print("You lose!")
                break

            guess = input("Write your guess: ").strip().lower()
            # input validation
            if not guess.isalpha():
                print("Please write a letter in alphabet")
                continue
            if guess in self.guessed_chars:
                print("You've already chosen that")
                continue

            self.guessed_chars.add(guess)
            self.check_ans(guess)
