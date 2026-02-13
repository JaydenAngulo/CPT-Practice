import math
original_code = input("Enter an 8 digit number: ")

def encryptor(a):
    digits = []
    encryption = []
    for i in original_code:
        digits.append(int(i))

    print(digits[:-1])
    print(enumerate(digits))
    
    for index, digit in enumerate(digits[:-1]):
        digit = int(digits[index])
        next_digit = int(digits[index + 1])
        if digit == 0:
            print(next_digit)
            adder_0 = digit + 578
            divider_0 = adder_0 / 34
            squarer_0 = divider_0 ** 2
            square_rooter_0 = math.sqrt(squarer_0)
            encryption.append(square_rooter_0)
            print(encryption)
            print(square_rooter_0)
            if next_digit == 1:
                print(int(square_rooter_0))
        elif digit == 1:
            adder_1 = digit + 951
            divider_1 = adder_1 / 119
            squared_1 = divider_1 ** 3
            second_divider_1 = int(squared_1 / 128)
            encryption.append(second_divider_1)
            print(encryption)
            print(second_divider_1)

encryptor(original_code)