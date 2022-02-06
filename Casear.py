alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
plain_text = input("Type your message:\n").lower()
shift_number = int(input("Type the shift number:\n"))

def casear (text,shift,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
     shift*= -1
    for letters in text:
      position= alphabet.index(letters)
      new_position=position+shift
      new_letters=alphabet[new_position]
      end_text+=new_letters
    print(f"Your result is here {end_text}")

casear(text=plain_text,shift=shift_number,cipher_direction=direction)
