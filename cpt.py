import math

"""
This function takes an 8 digit number and converts it into another
8 digit number by iterating through each digit after converting the
input into a list, changing each digit using "if" statements, and
arranging the digits into a different order.
"""

def encryptor(a):
    digits = []
    encryption = []
    # Loops through all the digits
    for i in a:
        # Adds the digits to a list
        digits.append(int(i))
    
    # Loops through the digits in the list
    for i in range(len(digits)):
        # The following if statements were written by Nicholas Whiney
        # Converts the number 0 if it is in the list
        if digits[i] == 0:
            adder = digits[i] + 578
            divider = adder / 34
            squarer = divider ** 2
            divider = squarer / 36
            subtracter = divider - 4.6294
            rounder = int(round(subtracter))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 1 if it is in the list
        if digits[i] == 1:
            adder = digits[i] + 951
            divider = adder / 119
            squared = divider ** 3
            divider = int(squared / 128)
            # Adds the new number to a list
            encryption.append(divider)
        # Converts the number 2 if it is in the list
        if digits[i] == 2:
            adder = digits[i] + 374
            divider = adder / 188
            power = divider ** 15
            divider = int(power / 32768)
            # Adds the new number to a list
            encryption.append(divider)
        # Converts the number 3 if it is in the list
        if digits[i] == 3:
            adder = digits[i] + 167
            divider = adder / 25
            adder = divider + 1
            power = adder ** 3
            divider = power / 81
            rounder = int(round(divider))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 4 if it is in the list
        if digits[i] == 4:
            adder = digits[i] + 842
            divider = adder / 141
            multiplier = divider * 524
            divider = multiplier / 97
            subtracter = divider - 55
            multiplier = subtracter * -2
            divider = multiplier / 8
            adder = divider + 3
            rounder = int(round(adder))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 5 if it is in the list
        if digits[i] == 5:
            adder = digits[i] + 502
            divider = adder / 39
            adder = divider + 1
            divider = int(adder / 2)
            # Adds the new number to a list
            encryption.append(divider)
        # Converts the number 6 if it is in the list
        if digits[i] == 6:
            adder = digits[i] + 6234
            divider = adder / 894
            subtracter = divider - 78
            power = subtracter ** 2
            divider = power / 5042
            subtracter = divider - 0.8342
            rounder = int(round(subtracter))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 7 if it is in the list
        if digits[i] == 7:
            adder = digits[i] + 7849
            divider = adder / 98
            subtracter = divider - 75
            rounder = int(round(subtracter))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 8 if it is in the list
        if digits[i] == 8:
            adder = digits[i] + 328
            divider = adder / 29
            power = divider ** 2
            divider = power / 51
            subtracter = divider - 0.4521
            rounder = int(round(subtracter))
            # Adds the new number to a list
            encryption.append(rounder)
        # Converts the number 9 if it is in the list
        if digits[i] == 9:
            adder = digits[i] + 638
            divider = adder / 39
            power = divider ** 2
            divider = power / 64
            multiplier = divider * 1.7534
            rounder = int(round(multiplier))
            # Adds the new number to a list
            encryption.append(rounder)
    
    # Rearranges the indexes of the digits in the list
    i, j = 0, 2
    encryption[i], encryption[j] = encryption[j], encryption[i]
    i, j = 1, 3
    encryption[i], encryption[j] = encryption[j], encryption[i]
    i, j = 4, 6
    encryption[i], encryption[j] = encryption[j], encryption[i]
    i, j = 5, 7
    encryption[i], encryption[j] = encryption[j], encryption[i]

    # Converts the list of digits into a single string
    encrypted_code = "".join(map(str, encryption))
    # Prints the string
    print("Here is your encrypted code:", encrypted_code)

"""
This function takes an 8 digit number that was already converted in
the previous funtion and it converts it back into the original 8
digit number by iterating through each digit after converting the
input into a list, changing each digit using "if" statements, and
arranging the digits back into the original order.
"""

def decryptor(a):
    digits = []
    decryption = []
    # Loops through all the digits
    for i in a:
        # Adds the digits to a list
        digits.append(int(i))
    # Rearranges the indexes of the digits in the list according to the encryptor function
    i, j = 0, 2
    digits[i], digits[j] = digits[j], digits[i]
    i, j = 1, 3
    digits[i], digits[j] = digits[j], digits[i]
    i, j = 4, 6
    digits[i], digits[j] = digits[j], digits[i]
    i, j = 5, 7
    digits[i], digits[j] = digits[j], digits[i]

    # Loops through all the digits in the list
    for i in range(len(digits)):
        # The following if statements were written by Nicholas Whiney
        # Converts the number 0 if it is in the list
        if digits[i] == 0:
            adder = digits[i] + 0.1662
            adder = adder + 0.8342
            multiplier = adder * 5042
            square_rooter = math.sqrt(multiplier)
            multiplier = square_rooter * (-1)
            adder = multiplier + 78
            multiplier = adder * 894
            subtracter = multiplier - 6234
            adder = subtracter + 1.2495
            rounder = int(round(adder))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 1 if it is in the list
        if digits[i] == 1:
            multiplier = digits[i] * 32768
            rooter = multiplier ** (1/15)
            multiplier = rooter * 188
            subtracter = int(multiplier - 374)
            # Adds the new number to a list
            decryption.append(subtracter)
        # Converts the number 2 if it is in the list
        if digits[i] == 2:
            adder = digits[i] + 0.1801
            adder = adder + 0.4521
            multiplier = adder * 51
            square_rooter = math.sqrt(multiplier)
            multiplier = square_rooter * 29
            subtracter = multiplier - 328
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 3 if it is in the list
        if digits[i] == 3:
            adder = digits[i] + 0.3984
            adder = adder + 4.6294
            multiplier = adder * 36
            square_rooter = math.sqrt(multiplier)
            multiplier = square_rooter * 34
            subtracter = multiplier - 578
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 4 if it is in the list
        if digits[i] == 4:
            multiplier = digits[i] * 128
            cube_rooter = math.cbrt(multiplier)
            multiplier = cube_rooter * 119
            subtracter = int(multiplier - 951)
            # Adds the new number to a list
            decryption.append(subtracter)
        # Converts the number 5 if it is in the list
        if digits[i] == 5:
            adder = digits[i] + 0.1633
            adder = adder + 75
            multiplier = adder * 98
            subtracter = multiplier - 7849
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 6 if it is in the list
        if digits[i] == 6:
            subtracter = digits[i] - 0.1413
            multiplier = subtracter * 81
            cube_rooter = math.cbrt(multiplier)
            subtracter = cube_rooter - 1
            multiplier = subtracter * 25
            subtracter = multiplier - 167
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 7 if it is in the list
        if digits[i] == 7:
            multiplier = digits[i] * 2
            subtracter = multiplier - 1
            multiplier = subtracter * 39
            subtracter = int(multiplier - 502)
            # Adds the new number to a list
            decryption.append(subtracter)
        # Converts the number 8 if it is in the list
        if digits[i] == 8:
            subtracter = digits[i] - 0.4681
            divider = subtracter / 1.7534
            multiplier = divider * 64
            square_rooter = math.sqrt(multiplier)
            multiplier = square_rooter * 39
            subtracter = multiplier - 638
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
        # Converts the number 9 if it is in the list
        if digits[i] == 9:
            subtracter = digits[i] - 0.3531
            subtracter = subtracter - 3
            multiplier = subtracter * 8
            divider = multiplier / -2
            adder = divider + 55
            multiplier = adder * 97
            divider = multiplier / 524
            multiplier = divider * 141
            subtracter = multiplier - 842
            rounder = int(round(subtracter))
            # Adds the new number to a list
            decryption.append(rounder)
    
    # Converts the list of digits into a single string
    decrypted_code = "".join(map(str, decryption))
    # Prints the string
    print("Here is your decrypted code:", decrypted_code)

print("Type 'Exit' to leave")
# Get an answer from the user to determine which function to run
answer = input("Do you want to encrypt or decrypt?: ")

# Runs the code as long as the user's answer isn't "Exit"
while answer != "Exit":
    # Checks if the user's answer is "encrypt"
    if answer.lower() == "encrypt":
        # Gets an 8 digit number from the user
        original_code = input("Enter an 8 digit number: ")
        # Runs the code as long as the user's answer is 8 digits long
        while len(original_code) != 8:
            # Gets an 8 digit number from the user
            original_code = input("Enter an 8 digit number: ")
        # Calls the funtion to print an encryption
        encryptor(original_code)
        # Stops the code
        break
    # Checks if the user's answer is "decrypt"
    elif answer.lower() == "decrypt":
        # Gets an 8 digit number from the user
        original_code = input("Enter an 8 digit number: ")
        # Runs the code as long as the user's answer is 8 digits long
        while len(original_code) != 8:
            # Gets an 8 digit number from the user
            original_code = input("Enter an 8 digit number: ")
        # Calls the funtion to print a decryption
        decryptor(original_code)
        # Stops the code
        break
    else:
        # Asks the user to choose either "encrypt" or "decrypt"
        answer = input("Please choose an answer: ")