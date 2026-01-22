def Pallindrome(n):
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

    Res = Pallindrome(No1)
    if Res == No1:
        print("number entered is Pallindrome:", Res)
    else:
        print("number entered is not Pallindrome:", Res)

if __name__ == "__main__":
    main()
