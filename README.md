# Simple Password Generator

A Python script to generate secure passwords 

## Features

- Generate multiple strong passwords at once
- Customizable password length
- Includes letters, numbers, and special symbols
- Easy to use interactive interface

## How to Use

1. Make sure you have Python installed (version 3.6 or higher)
2. Run the script:
   ```bash
   python3 script.py
   ```
3. Follow the prompts:
   - Enter desired password length (or press Enter for default 12)
   - Enter how many passwords to generate (or press Enter for default 5)
4. Your passwords will be displayed on screen

## Example Usage

```
Simple Password Generator
=========================
Enter password length (default 12): 16
How many passwords to generate (default 5): 3

Generated passwords:
-------------------
1. K9#mP2$vL8@nR4!
2. xQ7&wE5*zT3$bY9
3. F6%dH4&jU2#cN8$
```

## Security Notes

- Passwords are generated randomly using Python's `random` module
- For maximum security in production, consider using `secrets` module instead
- Never share your passwords with anyone
- Store passwords securely (password manager recommended)

## Requirements

- Python 3.6+
- No external dependencies needed

## Author

cat0x01
