def main():
    # NATO Phonetic Alphabet dictionary
    nato_alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    # Ask user for a word
    word = input("Enter a word to translate: ").upper()
    
    # Print each letter's NATO equivalent
    print("\nNATO Phonetic Translation:")
    for letter in word:
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
        else:
            print(f"'{letter}' is not a valid letter")

if __name__ == "__main__":
    main()