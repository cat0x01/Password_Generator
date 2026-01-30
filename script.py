#!/usr/bin/env python3
# Simple Password Generator for Beginners

import random
import string
import colorama 
from colorama import Fore, Style

colorama.init(autoreset=True)


banner = Fore.BLUE + """

 ██▓███   ▄▄▄        ██████   ██████   ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░  ░ ░   ░    ░      ░   ░ ░ 
               ░  ░      ░        ░        ░    ░  ░         ░ 
                                                               

[ + ] - Simple Password Generator [ + ]
[ + ] - Created by cat0x01 [ + ]
[ + ] - GitHub: @cat0x01 [ + ]


"""

print(banner)




def generate_password(length):
    # All possible characters
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all characters
    all_chars = letters + digits + symbols
    
    # Pick random characters
    password = ""
    for i in range(length):
        password += random.choice(all_chars)
    
    return password

def main():
    print(Fore.YELLOW +"Simple Password Generator")
    print("=========================")
    
    # Get password length from user
    length_input = input("Enter password length (default 12): ")
    
    # Use default if no input
    if length_input == "":
        length = 12
    else:
        length = int(length_input)
    
    # Get number of passwords
    count_input = input("How many passwords to generate (default 5): ")
    
    if count_input == "":
        count = 5
    else:
        count = int(count_input)
    
    print()
    print(Fore.GREEN + " Generated passwords:")
    print("-------------------")
    
    # Generate and print passwords
    for i in range(count):
        pwd = generate_password(length)
        print(f"{i+1}. {pwd}")

# Run the program
if __name__ == "__main__":
    main()
