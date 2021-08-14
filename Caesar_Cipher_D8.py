from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(text_encrypt, shift_amount):
#     cipher_text = ""
#     for letter in text_encrypt:
#        position = alphabet.index(letter) # list.index()
#        new_position = position + shift_amount
#        new_text = alphabet[new_position]
#        cipher_text += new_text
       
#     print(f"The encoded text is {cipher_text}")
    

# def decrypt(text_decrypt, shift_amount):
#     cipher_text = ""
#     for letter in text_decrypt:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_text = alphabet[new_position]
#         cipher_text += new_text
    
#     print(f"The decoded text is {cipher_text}")


def caesar(text_to_cipher, shift_amount, cipher_type):
    cipher_text = ""
    for letter in text_to_cipher:
        if letter in alphabet:
            position = alphabet.index(letter)
            
            if cipher_type == "encode":
                new_position = position + shift_amount
            elif cipher_type == "decode":
                new_position = position - shift_amount
            
            new_text = alphabet[new_position]
            cipher_text += new_text
        else:
            cipher_text += letter
        
    print(f"The {cipher_type}d text is: {cipher_text}")
    
    # if cipher_type == "encode":
    #     print(f"The encoded text is {cipher_text}")
    # elif cipher_type == "decode":
    #     print(f"The decoded text is {cipher_text}")
    
# if direction == "encode":
#     encrypt(text_encrypt=text, shift_amount= shift)
# elif direction == "decode":
#     decrypt(text_decrypt=text, shift_amount=shift)

want_to_continue = True
while want_to_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  

    caesar(text_to_cipher= text, shift_amount= shift, cipher_type= direction)
    
    caesar_cipher_command = input("Type 'Yes' if you want to go again, otherwise type 'No'\n").lower()
    if caesar_cipher_command == "no":
        want_to_continue = False
        print("Goodbye. Thank you!")

