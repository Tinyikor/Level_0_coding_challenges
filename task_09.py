def UniqueVowels(string):
    vowels =("aeiou")
    result =""
    for letter in string:
        letter = letter.lower()
        if (letter in vowels) and (letter not in result):
            result += letter
    print("Vowels: ", end="")
    print(*result, sep=" , ")

UniqueVowels("Umuzi")
