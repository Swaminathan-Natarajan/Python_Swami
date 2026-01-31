
def Prime(No):
    for i in range(2,No):
        if No % i == 0:
            return False
        else:
            return True
    
def main():
    print("Enter a number:")
    Num = int(input())
    
    Res = Prime(Num)
    if Res == True:
        print("It is a Prime Number", Num)
    elif Num == 1 or Num == 2:
        print("It is a Prime Number:", Num)
    else:
        print("It is not a prime number:", Num)

if __name__ == "__main__":
    main()