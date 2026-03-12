alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption():
    original_text=str(input("Enter the text:"))
    
    shift_amount=int(input("Enter the shift number:"))
    i=0
    encrypted_text=""
    for i in original_text:
        
        shifted_position=alphabets.index(i)+shift_amount
        if shifted_position > 25:
            shifted_position-=26
        
            encrypted_text +=alphabets[shifted_position]
        else:
            encrypted_text +=alphabets[shifted_position]
        
    print(encrypted_text)

def decode():
    original_text=str(input("Enter the text:"))
    
    shift_amount=int(input("Enter the shift number:"))
    i=0
    encrypted_text=""
    for i in original_text:
        
        shifted_position=alphabets.index(i)-shift_amount
        if shifted_position < 0 :
            new_shift=25-shifted_position+1
            
        
            encrypted_text +=alphabets[shifted_position]
        else:
            encrypted_text +=alphabets[shifted_position]
        
    print(encrypted_text)

choice=str(input("Do you want to encode or decode?"))
if choice=='encode':
    encryption()
elif choice=='decode':
    decode()
else:
    print("Invalid choice")

#ToDO 1 : create a function called ENCRYPTION ,that takes original text and shift amount as 2 inputs

#tODO 2: Inside the encrypt function, shifte each letter of originial text towards in the alphabetical order and print the encrypted text

#tODO 3: what happends if u shift alphabtes from z

#Todo 4: call the function and take user input

#Another way to do this:
