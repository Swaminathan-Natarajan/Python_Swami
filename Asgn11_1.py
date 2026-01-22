def Prime(No1):
    if No1 % 2 != 0:
        return True
    
def main():
    print("Enter the number :")
    No1 = int(input())

    Res = Prime(No1)

    if Res == True:
        print("Entered number is a prime number :", No1)
    else:
        print("Entered number is not a prime number :", No1)

if __name__ == "__main__":
    main()
