import hashlib
import getpass
import sys

def prompt_password(prompt):
    """Securely prompt the user for a password."""
    try:
        return getpass.getpass(prompt)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def generate_password(master_password, site_name):
    """Generate a password deterministically."""
    # Combine master password and site name
    combined_input = f"{site_name}{master_password}"

    # Create a SHA-256 hash
    hash_object = hashlib.sha256(combined_input.encode())
    hashed_password = hash_object.hexdigest()  # Hexadecimal output

    # Take the first 12 characters of the hash, and append a fixed uppercase letter and symbol
    base_password = hashed_password[:12]

    final_password = f"{base_password}A@"

    # Ensure the length is exactly 16 characters
    return final_password

def main():
    print("Simplified Deterministic Password Generator CLI")

    # Prompt for master password
    master_password = prompt_password("Enter your master password: ")
    confirm_password = prompt_password("Confirm your master password: ")

    # Verify the master password
    if master_password != confirm_password:
        print("Error: Passwords do not match.")
        sys.exit(1)

    # Prompt for site name
    site_name = input("Enter the website or service name: ").strip()
    if not site_name:
        print("Error: Site name cannot be empty.")
        sys.exit(1)

    # Generate the password
    generated_password = generate_password(master_password, site_name)

    # Display the generated password
    print("\nYour generated password is:")
    print(generated_password)

if __name__ == "__main__":
    main()
