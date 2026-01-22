def CountDigits(No1):
    count = 0
    for i in range(len(No1)):
        count = count + 1

    return count

    
def main():
    print("Enter the number :")
    No1 = input()

    Res = CountDigits(No1)

    print("Count of the digits of the number entered is:", Res)

if __name__ == "__main__":
    main()
