
PowOf2 = lambda num : 2 ** num

def main():
    print("Enter a number")
    num = int(input())

    Ret = PowOf2(num)

    print("Power of 2 of the number is:", Ret)

if __name__ == "__main__":
    main()