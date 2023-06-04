# Get the year input from the user
year = int(input("Which year do you want to check? "))

# Check if the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # If the year is divisible by 400, it is a leap year
            print("Leap year.")
        else:
            # If the year is divisible by 100 but not by 400, it is not a leap year
            print("Not a leap year.")
    else:
        # If the year is not divisible by 100 but divisible by 4, it is a leap year
        print("Leap year.")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("Not a leap year.")
