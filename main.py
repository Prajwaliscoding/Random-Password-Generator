import random
import string

def password_generator(length=12, use_digits=True, use_symbols=True,use_letters=True):
    if use_letters:
        letters=string.ascii_letters
    else:
        letters=""
    if use_digits:
        digits=string.digits
    else:
        digits=""
    if use_symbols:
        symbols=string.punctuation
    else:
        symbols=""
    all_chars=letters+digits+symbols

    password=""

    if not all_chars:
        return "No character types selected"
    
    for _ in range(length):
        password+=random.choice(all_chars)
    return password


def main():
    print("\nRandom Password Generator\n\n")
    length=int(input("Enter password length: "))
    use_digits=input("Do you want digits? ('y' for yes and 'n' for no): ").lower()=='y'
    use_symbols=input("Do you want symbols? ('y' for yes and 'n' for no): ").lower()=='y'
    use_letters=input("Do you want letter? ('y' for yes and 'n' for no): ").lower()=='y'
    print(f"{password_generator(length,use_digits,use_symbols,use_letters)}")

if __name__ == "__main__":
    main()