import art
from game import Game


def main():
    print("-----Welcome to Hangman-----")
    print()
    art.print_home()
    print("-------Topic: Fruits--------")
    input("Press Enter to play ")

    while True:
        game = Game()
        game.play()
        play_again = input("Do you want to play again?(y/n) ")
        if play_again.lower() == "n":
            print("Thanks for playing")
            break
        print()


if __name__ == "__main__":
    main()
