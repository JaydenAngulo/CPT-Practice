import math

def encryptor(a):
    digits = []
    encryption = []
    for i in original_code:
        digits.append(int(i))
    iterated_digits = iter(digits)
    
    for i in range(len(digits)):
        current_digit = int(i)
        next_digit = int(i + 1)
        previous_digit = int(i - 1)
        if digits[i] == 0:
            if next_digit == 1:
                adder = i + 945
                divider = adder / 5
                power = divider ** 2
                subtracter = power - 821
                divider = int(round(subtracter / 5784))
                encryption.append(divider)
                continue
            else:
                adder = i + 578
                divider = adder / 34
                squarer = divider ** 2
                square_rooter = int(math.sqrt(squarer))
                divider = square_rooter / 6
                rounded = int(round(divider))
                encryption.append(rounded)
        if digits[i] == 1:
            adder = i + 951
            divider = adder / 119
            squared = divider ** 3
            second_divider = int(squared / 128)
            encryption.append(second_divider)
        if digits[i] == 2:
            adder = i + 374
            divider = adder / 188
            power = divider ** 15
            second_divider = int(power / 32768)
            encryption.append(second_divider)
        if digits[i] == 3:
            adder = i + 167
            divider = adder / 25
            adder = divider + 1
            power = adder ** 3
            divider = int(round(power / 81))
            encryption.append(divider)
        if digits[i] == 4:
            adder = i + 842
            divider = adder / 141
            power = divider ** 2
            divider = power / 6
            multiplier = divider * 524
            divider = multiplier / 97
            subtracter = divider - 55
            multiplier = subtracter * -2
            divider = multiplier / 8
            adder = int(round(divider + 3))
            encryption.append(adder)
        if digits[i] == 5:
            adder = i + 502
            divider = adder / 39
            adder = divider + 1
            divider = int(round(adder / 2))
            encryption.append(divider)
    encrypted_code = "".join(map(str, encryption))
    print("Here is your encrypted code:", encrypted_code)

def decryptor(a):
    digits = []
    decryption = []
    print("Decryptor completed")

print("Type 'Exit' to leave")
answer = input("Do you want to encrypt or decrypt?: ")

while answer != "Exit":
    if answer.lower() == "encrypt":
        original_code = input("Enter an 8 digit number: ")
        while len(original_code) != 8:
            original_code = input("Enter an 8 digit number: ")
        encryptor(original_code)
        yes_or_no = input("Do you want to decrypt this code?: ")
        if yes_or_no == "yes":
            decryptor(encryptor(original_code))
        if yes_or_no == "no":
            break
    elif answer.lower() == "decrypt":
        original_code = input("Enter an 8 digit number: ")
        while len(original_code) != 8:
            original_code = input("Enter an 8 digit number: ")
        decryptor(original_code)
        break
    else:
        answer = input("Please choose an answer: ")