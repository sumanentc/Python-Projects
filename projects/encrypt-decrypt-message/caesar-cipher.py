from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(plan_text, shift_amount, direction):
    caesar_message = ''
    shift_amount = shift_amount % 26
    for char in plan_text:
        if char in alphabet:
            letter_pos = alphabet.index(char)
            if 'encode' == direction:
                new_position = (letter_pos + shift_amount) % 25
            else:
                new_position = (letter_pos - shift_amount) % 25
            caesar_message += alphabet[new_position]
        else:
            caesar_message += char
    return caesar_message


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if 'encode' == direction.lower():
        encrypted_message = caesar(plan_text=text, shift_amount=shift, direction='encode')
        print(f"The encoded text is {encrypted_message}")
    elif 'decode' == direction.lower():
        decrypted_message = caesar(plan_text=text, shift_amount=shift, direction='decode')
        print(f"The decoded text is {decrypted_message}")
    else:
        print('Invalid encrypt/decrypt direction')
    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if replay == "no":
        should_continue = False
        print("Goodbye")
