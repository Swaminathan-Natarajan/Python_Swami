def SumOfDigits(No1):
    Ret = sum(map(int,No1))

    return Ret

    
def main():
    print("Enter the number :")
    No1 = input()

    Res = SumOfDigits(No1)

    print("Sum of the digits of the number entered is:", Res)

if __name__ == "__main__":
    main()
