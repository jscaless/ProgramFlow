numbers = [1, 45, 32, 12, 60]

for numbers in numbers:
    if numbers % 8 == 0:
        # reject the loop
        print("The number modular difference is unacceptable.")
        break
else:
    print("All those numbers are fine.")