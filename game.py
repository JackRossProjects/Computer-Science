
    # Guessing game

    # What are the rules?
        # Write a program that plays a guessing game with the user
        # The user will think of a number and the program has to guess it
        # Range of possible numbers in between 1 and 100
        # Program prints out rules at start
        # Player says "low" "high" or "equal" to guess

        
guess_correct = False
floor = 1
ceiling = 100        

print("\nThink of a number between 1 and 100 and I will guess it!")
print("After each guess, tell me if the guess was high, low, or equal to your number!\n")

while not guess_correct:
    guess = (floor + ceiling) // 2
    print(f"My guess: {guess}")
    result = input("\nWas my guess high, low, or equal: ")
    result = result.lower()
    result = result[0]

    if result == 'h':
        ceiling = guess - 1
    elif result == 'l':
        floor = guess + 1
    elif result == 'e':
        print("\nI guessed your number!")
        guess_correct = True
    else:
        print("Try again...\n")
