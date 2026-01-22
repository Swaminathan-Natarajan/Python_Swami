def Reverse(n):
    rev = 0
    d = None
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n //= 10
    return rev    


    
def main():
    print("Enter the number :")
    No1 = int(input())

    Res = Reverse(No1)

    print("Reverse of the digits of the number entered is:", Res)

if __name__ == "__main__":
    main()
