# Experiment 18: Check whether a mobile number is valid
def is_valid_mobile(number):
    if len(number) == 10 and number[0] in ['7', '8', '9'] and number.isdigit():
        return True
    else:
        return False

mobile = input("Enter your mobile number: ")

if is_valid_mobile(mobile):
    print("Valid mobile number.")
else:
    print("Invalid mobile number.")
