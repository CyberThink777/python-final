from word import get_word


class Game:
    def __init__(self):
        super().__init__()
        self.word = get_word()
        self.state = 0

    def play(self):
        print(self.word)
        print(self.state)
