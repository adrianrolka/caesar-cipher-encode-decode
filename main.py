alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art

print(art.logo)
def caesar(text, shift, direction):
  coded_text = ""
  for el in text:
    if el not in alphabet:
      coded_text += el
    else:
      i = alphabet.index(el)
      if direction == "encode":
        if shift > 26:
          shift = shift % 26
        if i + shift > 25:
            nowy = alphabet[(shift - (25 - i))-1]
            coded_text += nowy
        else:
            coded_litera = alphabet[i + shift]
            coded_text += coded_litera   
      elif direction == "decode":
          coded_litera = alphabet[i - shift]
          coded_text += coded_litera
    
  print(f"Here's the {direction}d result: {coded_text}")
  
continue_code = "yes"
while continue_code == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(text,shift,direction)
  continue_code = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")