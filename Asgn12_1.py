def Vowel(char):
    str = "aeiouAEIOU"
    if char in str:
        return True
    else:
        return False

def main():
    print("Enter the char :")
    char = input()

    Res = Vowel(char)
    if Res == True:
        print("Entered char is a Vowel:", char)
    else:
        print("Entered chat is a consonant:", char)


if __name__ == "__main__":
    main()