
MinNum = lambda No1, No2 : No1<No2


def main():
    print("Enter a Number")
    No1 = int(input())

    print("Enter a Number")
    No2 = int(input())

    Res = MinNum(No1, No2)

    if Res == True:
        print("Min Number is No1: ", No1)
    else:
        print("Min Number is No2:", No2)


if __name__ == "__main__":
    main()

