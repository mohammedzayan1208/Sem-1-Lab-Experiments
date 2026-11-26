# Experiment 3: Calculate the electricity bill for two months

FAN_CONSUMPTION = 1
LIGHT_CONSUMPTION = 0.5
WASHING_MACHINE_CONSUMPTION = 2
COMPUTER_CONSUMPTION = 3
COST_PER_UNIT = 50
DAYS_IN_MONTH = 30
MONTHS = 2

fans = int(input("Enter the number of fans: "))
lights = int(input("Enter the number of lights: "))
washing_machines = int(input("Enter the number of washing machines: "))
computers = int(input("Enter the number of computers: "))

total_daily_consumption = (
    fans * FAN_CONSUMPTION
    + lights * LIGHT_CONSUMPTION
    + washing_machines * WASHING_MACHINE_CONSUMPTION
    + computers * COMPUTER_CONSUMPTION
)
total_consumption = total_daily_consumption * DAYS_IN_MONTH * MONTHS
total_bill = total_consumption * COST_PER_UNIT

print("The total electricity bill for 2 months is:", total_bill, "rupees.")
