from generate_password import generate_password

def generate_multiple_passwords(num_passwords=5, max_retries=10):
    """
    Generates multiple passwords, ensuring they contain both upper and lower case characters.
    """
    passwords = []
    for _ in range(num_passwords):
        retries = 0
        while retries < max_retries:
            password = generate_password()
            if password != "Could not generate a password." and any(c.isupper() for c in password) and any(c.islower() for c in password):
                passwords.append(password)
                break
            retries += 1
        else:
            print("Warning: Could not generate a valid password after several retries.")
    return passwords

if __name__ == "__main__":
    passwords = generate_multiple_passwords()
    if passwords:
        print("Generated passwords:")
        for password in passwords:
            print(password)
