def check_vowel_or_consonant(char):
    char=char.lower()
    if char in ['a','e','i','o','u']:
        return f"{char} is a vowel."
    else:
        return f"{char} is a consonant."
user_char=input("enter a character")
result=check_vowel_or_consonant(user_char)
print(result)

      