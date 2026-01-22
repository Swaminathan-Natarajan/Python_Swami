
EvenCheck = lambda No1: No1%2==0


def main():
    print("Enter a Number")
    No1 = int(input())

    Res = EvenCheck(No1)

    if Res == True:
        print("Even Number: ", No1)
    else:
        print("Odd Number:", No1)


if __name__ == "__main__":
    main()

