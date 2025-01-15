def robot(sticks):
    if sticks % 4 == 0:
        # If the number of remaining sticks is a multiple of 4,
        # taking 1 stick keeps the total remaining a multiple of 4
        return 1
    else:
        # If remaining sticks are not multiple of 4,
        # the bot takes enough sticks to make the total a multiple of 4
        return sticks % 4

def play_game():
    sticks = 21
    current_player = "Bot"  # Start with the bot

    print("21 sticks in the pile.")

    while sticks > 0:
        if current_player == "Bot":
            take = robot(sticks)
            print(f"Player 1 (Bot) takes: {take}")
            sticks -= take
            print(f"{sticks} sticks in the pile.")

            if sticks == 0:
                print("Player 1 (Bot) won!")
                break

            current_player = "User"
        else:
            print("Player 2 takes:")
            try:
                take = int(input())  # Assume valid input between 1-3
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 3.")
                continue

            # Ensure player doesn't take more sticks than available
            if take < 1 or take > 3 or take > sticks:
                print("Invalid move! You can take 1 to 3 sticks, or not more than the remaining sticks.")
                continue

            sticks -= take
            print(f"{sticks} sticks in the pile.")

            if sticks == 0:
                print("Player 2 won!")
                break

            current_player = "Bot"

def main():
    play_game()

if __name__ == "__main__":
    main()
