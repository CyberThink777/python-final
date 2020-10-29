import art as art

def main():
    print("-----Welcome to Hangman-----")
    print()
    art.print_home()
    print("----------------------------")

    while True:
        play_again = input("Do you want to play again?")
        if play_again.lower() == "n":
            break
    else: 
        print("Thanks for playing")

if __name__ == "__main__":
    main()
