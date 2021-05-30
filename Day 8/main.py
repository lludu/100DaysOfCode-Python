from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_program = True
print (logo)



def caesar(start_text, shift_amount, ceasar_direction):
  ciphered = []
  if ceasar_direction == "decode":
    shift_amount *= -1
  for character in start_text:
    if character in alphabet:
      alpha_position = (alphabet.index(character))
      alpha_shifted = alpha_position + shift_amount
      if alpha_shifted > 25:
        alpha_shifted = alpha_shifted - 26
      ciphered.append(alphabet[alpha_shifted])
    else:
      ciphered.append(character)
      
  ciphered = ''.join(ciphered)
  print(f'\nThe {ceasar_direction}d result is:\n{ciphered.capitalize()}')
  

while run_program:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction == 'encode' or direction == 'decode':
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number: "))

    if shift > 26:
      shift = shift % 26
      print(shift)

    caesar(start_text=text, shift_amount=shift, ceasar_direction=direction)
  else:
    print('That response was invalid\n')
  
  restart = input('\nWould you like to continue ciphering? ').lower()
  if restart == 'yes' or restart == 'y':
    run_program = True
  elif restart =='no' or restart == 'n':
    print('Thanks for using the ceasar cipher, goodbye!')
    run_program = False
  else:
    print('You have made an invalid response, goodbye!')
    run_program = False
