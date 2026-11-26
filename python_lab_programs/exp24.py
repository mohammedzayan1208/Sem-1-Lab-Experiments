# Experiment 24: Sticks Game
sticks = 16
player = 1

print("Welcome to the Sticks Game!")
print("Rules: On your turn, pick 1, 2, or 3 sticks. The player who takes the last stick loses.\n")

while sticks > 0:
    print("Remaining sticks:", sticks)

    try:
        pick = int(input("Player " + str(player) + ", pick 1, 2, or 3 sticks: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if pick < 1 or pick > 3:
        print("Invalid choice! You can pick only 1, 2, or 3 sticks.")
        continue
    if pick > sticks:
        print("Invalid choice! Only " + str(sticks) + " sticks remaining.")
        continue

    sticks -= pick

    if sticks == 0:
        print("\nPlayer", player, "took the last stick and loses!")
        break

    if player == 1:
        player = 2
    else:
        player = 1
