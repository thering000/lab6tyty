# first  first github addition


def encoder(password):
    encoded_password = ""
    
    # Check if the password is valid
    if not (password.isdigit() and len(password) == 8):
        return "Invalid password. Please enter an 8-digit password containing only integers."
    
    # Encode the password by shifting each digit up by 3 numbers
    for digit in password:
        # Calculate the new digit after shifting and handle the overflow
        new_digit = (int(digit) + 3) % 10  
        encoded_password += str(new_digit)
    
    return encoded_password

def decoder(encoded_password):
    pass  # This function is left intentionally blank

def main():
    while True:
        # Display the menu to the user
        print("\n1. Encoder")
        print("2. Decoder")
        print("3. Exit")
        choice = input("Please choose an option (1/2/3): ")
        
        if choice == '1':
            password = input("Please enter an 8-digit password: ")
            print(f"Encoded password: {encoder(password)}")
        elif choice == '2':
            print("Decoder function is not implemented yet.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
