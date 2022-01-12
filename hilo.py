import time

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:  # while True, creates infinite loop, just like continue. Cannot do while guess =! answer, we don't know answer.
    # print("\tGuessing in the range of {} and {} ".format(low,high))
    # time.sleep(1) # Adds a timer to execute code
    guess = low + (high - low) // 2  # Binary Search Formula
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if I'm correct. "
                     .format(guess)).casefold()  # Casefold removes case distinctions

    if high_low == "h":
        low = guess + 1
        # pass # Dummy Code to Syntactically correct to work.
        # Guess higher. The low end of the range becomes 1 greater than the guess.
    elif high_low == "l":
        high = guess - 1
        # pass # Dummy Code to Syntactically correct to work.
        # Guess lower. The high end of the range becomes 1 lesser than the guess.
    elif high_low == "c":
        print("I got it in {} amount of guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, c")

    # guesses = guesses + 1 # Augmented Assignment is guesses += 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))

