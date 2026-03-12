alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # Move the shift adjustment OUTSIDE the loop
    if encode_or_decode == 'decode':
        shift_amount *= -1
        
    for letter in original_text:
        if letter in alphabets: # Added check for spaces/numbers
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter # Keeps spaces/symbols as they are

    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Match the variable names here to the function definition

should_continue=True
while should_continue:
    
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    text = input("Type your text: ").lower()
    shift = int(input("Enter the shift number: ")) # Added int()
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Wanna try again:")
    if restart=='yes':
        ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    else:
        should_continue=False
        print("goodbye")
