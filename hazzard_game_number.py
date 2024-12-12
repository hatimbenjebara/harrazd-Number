import numpy as np
# Generate a random integer between 1 and 1000
random_number = np.random.randint(1, 1001)
print("Guess the number (between 1 and 1000):")
while True:
    try:
        # Get user input and convert it to an integer
        user_guess = int(input("Enter your guess: "))        
        # Check if the guess is in the valid range
        if user_guess < 1 or user_guess > 1000:
            print("Please enter a number between 1 and 1000.")
            continue   
        # Compare the user's guess with the random number
        if user_guess < random_number:
            print("Your number is too low, try again!")
        elif user_guess > random_number:
            print("Your number is too high, try again!")
        else:
            print("Bravo! You guessed it!")
            break  # Exit the loop if guessed correctly
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

