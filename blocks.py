# for i in range(1, 13):
    # print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    # print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
print("Thank you for your information {0}, we now know that you are {1} years old!".format(name, age))

# if age >= 18: # Cmd + / is a mass remove.
#     print("You are old enough to vote.")
#     print("Please mark a X within the ballot box")
# else:
#     print("You are not old enough to vote. Please come back in {0} years".format(18 - age))

if age < 18:
    print("You are not old enough to vote. Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Methusda, go back to the Bible Ages!")
elif age == 1000:
    print("Josh stop playing with Lord of the Rings ages!")
else:
    print("You are old enough to vote.")
    print("Please mark a X within the ballot box")