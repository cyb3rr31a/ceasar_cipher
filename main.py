from art import logo

# This is a simple ceasar cipher program that encrypts and decrypts a message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def ceasar(text, shift, direction):
    new_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            new_position = new_position % 26
            new_text += alphabet[new_position]

        else:
            new_text += letter

    print(f"The {direction}d text is {new_text}")

gameover = False

while gameover == False:
    direction = input("Type 'encode` to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)

    gameover = input("Do you want to play again? 'yes' or 'no' ").lower()
    if gameover == "no":
        gameover = True
        print("Goodbye")
    elif gameover == "yes":
        gameover = False
        ceasar(text, shift, direction)
    else:
        print("Invalid input")
        gameover = False
