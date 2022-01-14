def common(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    common_letters =""
    for i in string_1:
        if i in string_2:
            common_letters = common_letters + i
    letter = ""
    for i in common_letters:
        if i not in letter:
            letter = letter + i
    print ("Common letters: ", end="")
    print (*letter, sep=",")

common("house", "computers")
