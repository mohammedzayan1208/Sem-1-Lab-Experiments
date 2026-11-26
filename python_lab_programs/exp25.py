# Experiment 25: Monty Hall problem simulation
import random

def monty_hall_simulation(trials):
    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):
        doors = [0, 0, 0]  # 0 = goat, 1 = car
        car_position = random.randint(0, 2)
        doors[car_position] = 1

        player_choice = random.randint(0, 2)

        # Host opens a goat door that the player did not choose.
        remaining_doors = [
            i for i in range(3)
            if i != player_choice and doors[i] == 0
        ]
        host_opens = random.choice(remaining_doors)

        switch_choice = [
            i for i in range(3)
            if i != player_choice and i != host_opens
        ][0]

        if doors[player_choice] == 1:
            stay_wins += 1
        if doors[switch_choice] == 1:
            switch_wins += 1

    stay_percentage = (stay_wins / trials) * 100
    switch_percentage = (switch_wins / trials) * 100

    print("Monty Hall Simulation Results after", trials, "trials:")
    print("Staying with initial choice: Wins =", stay_wins,
          ", Winning Percentage =", round(stay_percentage, 2), "%")
    print("Switching to other door: Wins =", switch_wins,
          ", Winning Percentage =", round(switch_percentage, 2), "%")

trials = int(input("Enter number of trials: "))
if trials > 0:
    monty_hall_simulation(trials)
else:
    print("Enter a positive number of trials.")
