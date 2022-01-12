challenge_options = "\n1.\tLearn Python \n2.\tLearn Java \n3.\tGo Swimming" \
                    "\n4.\tHave Dinner \n5.\tGo to Bed \n0.\tExit "
print("Please choose your option from the list below: {} ".format(challenge_options))
challenge_input = '-'
while True:
    challenge_input = input()
    # if challenge_input == "0":
    #     break
    # elif challenge_input in "12345":
    #     print("You chose {}".format(challenge_options))
    if challenge_input == '1':
        print('Learning Python Started')
    elif challenge_input == '2':
        print('Learning Java Started')
    elif challenge_input == '3':
        print('Swimming Started')
    elif challenge_input == '4':
        print('Having Dinner Started')
    elif challenge_input == '5':
        print('Going to Bed')
    elif challenge_input == '0':
        print("Exiting Options")
        break
    else:
        print(challenge_options)
