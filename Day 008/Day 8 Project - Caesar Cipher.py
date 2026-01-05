import logo
print(logo.logo)

alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#
#     for letter in original_text:
#         shifted_pos = alphabets.index(letter) + shift_amount
#         shifted_pos %= len(alphabets)
#         cipher_text += alphabets[shifted_pos]
#     print(f"Here is your encoded results: {cipher_text}")
#
# def decrypt(original_text, shift_amount):
#     output_text = ""
#
#     for letter in original_text:
#         shifted_pos = alphabets.index(letter) - shift_amount
#         shifted_pos %= len(alphabets)
#         output_text += alphabets[shifted_pos]
#     print(f"Here is your encoded results: {output_text}")

def caser(original_text, shift_amount, encode_decode):
    output_text = ""

    actual_shift = -shift_amount if encode_decode == "decode" else shift_amount

    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_pos = alphabets.index(letter) + actual_shift
            shifted_pos %= len(alphabets)
            output_text += alphabets[shifted_pos]
    print(f"Here is your {encode_decode}d results: {output_text}")


should_Continue = True
while should_Continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: \n").lower()
    text = input("Type your message : \n").lower()
    shift = int(input("Type Shift Number : \n"))

    caser(original_text= text, shift_amount= shift, encode_decode= direction)
    # encrypt(original_text= text, shift_amount= shift)
    # decrypt(original_text= text, shift_amount= shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    if restart == "no":
        should_Continue = False
        print("GoodBye!!")
