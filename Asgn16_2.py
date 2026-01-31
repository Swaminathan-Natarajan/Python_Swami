def ChkNum(No):
    if No % 2 == 0:
        return True

def main():
    print("Enter a Number:")
    No = int(input())
    Res = ChkNum(No)

    if Res == True:
        print("Even Number:", No)
    else:
        print("Odd Number:", No)

if __name__ == "__main__":
    main()