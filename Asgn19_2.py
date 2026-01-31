
Mult = lambda num, num1 : num1 * num

def main():
    print("Enter 1st number")
    num = int(input())

    print("Enter 2nd number")
    num1 = int(input())

    Ret = Mult(num, num1)

    print("Multiplication is:", Ret)

if __name__ == "__main__":
    main()