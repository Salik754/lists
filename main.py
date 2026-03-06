# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def shift_letters(message, shift):
    # Create an empty list to store the shifted characters  
    shifted_chars = []
    # Loop through each character in the string:
    for char in message:
        # If the character is a letter (A-Z or a-z):
        if char.isalpha():
            # Shift the letter by adding the shift value to its ASCII code (use the ord function)
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # Add the shifted character to the list
            shifted_chars.append(shifted_char)
        else:
            # If the character is not a letter, add it unchanged to the list
            shifted_chars.append(char)
    # After the loop, join the list into a string and return it
    return ''.join(shifted_chars)

# Get user input for the message and shift value  
message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

# Call the function with the inputs and display the result
result = shift_letters(message, shift)
print("Shifted message:", result)
#        Add the shifted character to the list

#    If the character is not a letter:
#        Add the character unchanged to the list
# After the loop, join the list into a string and return it  
# Get user input for the message and shift value  
# Call the function with the inputs and display the result