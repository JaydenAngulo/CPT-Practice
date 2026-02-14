import math

def encryptor(a):
    digits = []
    encryption = []
    for i in a:
        digits.append(int(i))
    iterated_digits = iter(digits)
    
    for i in range(len(digits)):
        current_digit = int(i)
        next_digit = int(i + 1)
        previous_digit = int(i - 1)
        print(current_digit, next_digit, previous_digit)
        if digits[i] == 0:
            # if current_digit == 0:
            #     adder = i + 945
            #     divider = adder / 5
            #     power = divider ** 2
            #     subtracter = power - 821
            #     divider = int(round(subtracter / 5784))
            #     encryption.append(divider)
            #     continue
            # else:
            adder = digits[i] + 578
            divider = adder / 34
            squarer = divider ** 2
            divider = squarer / 36
            subtracter = divider - 4.6294
            rounder = int(round(subtracter))
            encryption.append(rounder)
        if digits[i] == 1:
            adder = digits[i] + 951
            divider = adder / 119
            squared = divider ** 3
            divider = int(squared / 128)
            encryption.append(divider)
        if digits[i] == 2:
            adder = digits[i] + 374
            divider = adder / 188
            power = divider ** 15
            divider = int(power / 32768)
            encryption.append(divider)
        if digits[i] == 3:
            adder = digits[i] + 167
            divider = adder / 25
            adder = divider + 1
            power = adder ** 3
            divider = power / 81
            rounder = int(round(divider))
            encryption.append(rounder)
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
            encryption.append(rounder)
        if digits[i] == 5:
            adder = digits[i] + 502
            divider = adder / 39
            adder = divider + 1
            divider = int(adder / 2)
            encryption.append(divider)
        if digits[i] == 6:
            adder = digits[i] + 6234
            divider = adder / 894
            subtracter = divider - 78
            power = subtracter ** 2
            divider = power / 5042
            subtracter = divider - 0.8342
            rounder = int(round(subtracter))
            encryption.append(rounder)
        if digits[i] == 7:
            adder = digits[i] + 7849
            divider = adder / 98
            subtracter = divider - 75
            rounder = int(round(subtracter))
            encryption.append(rounder)
        if digits[i] == 8:
            adder = digits[i] + 328
            divider = adder / 29
            power = divider ** 2
            divider = power / 51
            subtracter = divider - 0.4521
            rounder = int(round(subtracter))
            encryption.append(rounder)
        if digits[i] == 9:
            adder = digits[i] + 638
            divider = adder / 39
            power = divider ** 2
            divider = power / 64
            multiplier = divider * 1.7534
            rounder = int(round(multiplier))
            encryption.append(rounder)

    encrypted_code = "".join(map(str, encryption))
    print("Here is your encrypted code:", encrypted_code)

def decryptor(a):
    digits = []
    decryption = []
    for i in a:
        digits.append(int(i))
    iterated_digits = iter(digits)

    for i in range(len(digits)):
        current_digit = int(i)
        next_digit = int(i + 1)
        previous_digit = int(i - 1)
        print(current_digit, next_digit, previous_digit)
        if digits[i] == 0:
            adder = digits[i] + 0.1662
            adder = adder + 0.8342
            multiplier = adder * 5042
            square_rooter = math.sqrt(multiplier)
            print(square_rooter)
            adder = square_rooter + 78
            multiplier = adder * 894
            subtracter = multiplier - 6234
            rounder = int(round(subtracter))
            decryption.append(rounder)
        if digits[i] == 1:
            multiplier = digits[i] * 32768
            rooter = multiplier ** (1/15)
            multiplier = rooter * 188
            subtracter = int(multiplier - 374)
            decryption.append(subtracter)
        if digits[i] == 2:
            adder = digits[i] + 374
            divider = adder / 188
            power = divider ** 15
            divider = int(power / 32768)
            decryption.append(divider)
        if digits[i] == 3:
            adder = digits[i] + 0.3984
            adder = adder + 4.6294
            multiplier = adder * 36
            square_rooter = math.sqrt(multiplier)
            multiplier = square_rooter * 34
            subtracter = multiplier - 578
            rounder = int(round(subtracter))
            decryption.append(rounder)
        if digits[i] == 4:
            multiplier = digits[i] * 128
            cube_rooter = math.cbrt(multiplier)
            multiplier = cube_rooter * 119
            subtracter = int(multiplier - 951)
            decryption.append(subtracter)
        if digits[i] == 5:
            adder = digits[i] + 502
            divider = adder / 39
            adder = divider + 1
            divider = adder / 2
            rounder = int(round(divider))
            decryption.append(rounder)
        if digits[i] == 6:
            subtracter = digits[i] - 0.1413
            multiplier = subtracter * 81
            cube_rooter = math.cbrt(multiplier)
            subtracter = cube_rooter - 1
            multiplier = subtracter * 25
            subtracter = multiplier - 167
            rounder = int(round(subtracter))
            decryption.append(rounder)
        if digits[i] == 7:
            multiplier = digits[i] * 2
            subtracter = multiplier - 1
            multiplier = subtracter * 39
            subtracter = int(multiplier - 502)
            decryption.append(subtracter)
        if digits[i] == 8:
            adder = digits[i] + 328
            divider = adder / 29
            power = divider ** 2
            divider = power / 51
            subtracter = divider - 0.4521
            rounder = int(round(subtracter))
            decryption.append(rounder)
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
            decryption.append(rounder)
    
    decrypted_code = "".join(map(str, decryption))
    print("Here is your decrypted code:", decrypted_code)

print("Type 'Exit' to leave")
answer = input("Do you want to encrypt or decrypt?: ")

while answer != "Exit":
    if answer.lower() == "encrypt":
        original_code = input("Enter an 8 digit number: ")
        while len(original_code) != 8:
            original_code = input("Enter an 8 digit number: ")
        encryptor(original_code)
        break
    elif answer.lower() == "decrypt":
        original_code = input("Enter an 8 digit number: ")
        while len(original_code) != 8:
            original_code = input("Enter an 8 digit number: ")
        decryptor(original_code)
        break
    else:
        answer = input("Please choose an answer: ")