def IsPerfectNumber(No):
    num = 0
    for i in range(1,No):
        if(No % i) == 0:
            num = num + i

    if num == No:
        return True


    

def main():
    print("Enter the number :")
    No = int(input())


    Res = IsPerfectNumber(No)

    if Res == True:
        print("Number Entered is a Perfect number:", No)
    else:
        print("Not a Perfect number :", No)
    


if __name__ == "__main__":
    main()