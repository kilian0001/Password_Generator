#Coded by kilian.01. Please give credits if youre going to use it for you own projects.
#Otherwise feel free to use it. If you have some issus report them please, it helps me a lot

#Dont forget to run the requirements.txt 

#pip install -r requirements.txt

import random
import string
import sys
import pyperclip #dont worry if it shows as not installed. It has to work:)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, language):
    characters = ""

    if length > 50:
        print("\n" + ("Length will be set to 50!!!" if language == 'en' else "Die Länge wird auf 50 herunter gesetzt!!!"))
        length = 50

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("\n" + ("Please select at least one character category." if language == 'en' else "Bitte wählen Sie mindestens eine Zeichenkategorie aus."))
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password, language):
    length = len(password)
    if length < 2:
        return ("Too Weak\n" if language == 'en' else "Zu Schwach\n")
    elif 2 <= length < 8:
        return ("Weak\n" if language == 'en' else "Schwach\n")
    elif 8 <= length < 12:
        return ("Moderate\n" if language == 'en' else "Mäßig\n")
    elif 12 <= length < 20:
        return ("Strong\n" if language == 'en' else "Stark\n")
    else:
        return ("Very Strong\n" if language == 'en' else "Sehr Stark\n")

def choose_language():
    language = input("Choose your language (en for English, de for German): ").lower()
    return language

def main():

    ascii_art = """
 ___                                  _  ___                             _            
| . \ ___  ___ ___ _ _ _  ___  _ _  _| |/  _>  ___ ._ _  ___  _ _  ___ _| |_ ___  _ _ 
|  _/<_> |<_-<<_-<| | | |/ . \| '_>/ . || <_/\/ ._>| ' |/ ._>| '_><_> | | | / . \| '_>
|_|  <___|/__//__/|__/_/ \___/|_|  \___|`____/\___.|_|_|\___.|_|  <___| |_| \___/|_|  
                                                                                       
    """
    sys.stdout.write("\x1b]2;Kilian01 I PasswordGenerator\x07")
    language = choose_language()
    print(ascii_art)

    length = int(input("\n" + ("Enter the desired password length: " if language == 'en' else "Geben Sie die gewünschte Passwortlänge ein: ")))
    use_uppercase = input(("Use uppercase letters? (Yes/No): " if language == 'en' else "Großbuchstaben verwenden? (Ja/Nein): ")).lower() == 'yes' or 'ja'
    use_lowercase = input(("Use lowercase letters? (Yes/No): " if language == 'en' else "Kleinbuchstaben verwenden? (Ja/Nein): ")).lower() == 'yes' or 'ja'
    use_numbers = input(("Use numbers? (Yes/No): " if language == 'en' else "Zahlen verwenden? (Ja/Nein): ")).lower() == 'yes' or 'ja'
    use_special_chars = input(("Use special characters? (Yes/No): " if language == 'en' else "Sonderzeichen verwenden? (Ja/Nein): ")).lower() == 'yes' or 'ja'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars, language)

    if password:
        print("\n" + (("Generated Password:" if language == 'en' else "Generiertes Passwort:")), password)
        try:
            pyperclip.copy(password)
            print((("The password has been copied to the clipboard." if language == 'en' else "Das Passwort wurde in die Zwischenablage kopiert.")))
        except Exception as e:
            print((("Error copying to clipboard:" if language == 'en' else "Fehler beim Kopieren in die Zwischenablage:")), str(e))
        strength = password_strength(password, language)
        print("\n" + (("Password Strength:" if language == 'en' else "Passwortsicherheit:")), strength)
    print("\n" + (("This script will wait for user input before closing the CMD window." if language == 'en' else "Das Fenster schließt sich wenn du die Enter Taste betätigst")))
    user_input = input((("Press Enter to exit..." if language == 'en' else "Betätige die Enter Tast um das Fenster zu schließen...")))


if __name__ == "__main__":
    main()
