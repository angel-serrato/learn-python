alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art_main import cipher
print("--------------------------------------------------")
print(cipher)
print("Welcome to Ceaser Cipher project.")
print("--------------------------------------------------")

def caesar(original_text, shift_ammount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_ammount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift_ammount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result {output_text}.")

should_continue = True

while should_continue:
    direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Please enter either 'encode' or 'decode'.")
        direction = input(f"Type 'encode' to encrypt, type 'decode'?\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_ammount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_continue = False
        print("Thank you for using Ceaser Cipher project.")
