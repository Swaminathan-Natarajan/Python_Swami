def Factorial(No1):
    
    val = 1
    for i in range(1,No1+1):
        val = val*i

    return val


def main():
    print("Enter the number:")
    No1 = int(input())

    Res = Factorial(No1)

    print("Factorial of number entered is :", Res)

if __name__ == "__main__":
    main()