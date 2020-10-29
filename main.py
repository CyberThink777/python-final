import art as art
from game import Game


def main():
    print("-----Welcome to Hangman-----")
    print()
    art.print_home()
    print("-------Topic: Fruits--------")
    input("Press Enter to play")

    while True:
        game = Game()
        game.play()
        play_again = input("Do you want to play again?(y/n) ")
        if play_again.lower() == "n":
            break
    else:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
