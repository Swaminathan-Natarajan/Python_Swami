def ChkGreater(No1, No2):
    if No1 > No2:
        return True
    else:
        return False
        

def main():
    print("Enter the first number :")
    No1 = int(input())
    print("Enter the second number :")
    No2 = int(input())
    Res = ChkGreater(No1, No2)
    if Res == True:
        print("No1 is Greater :", No1)
    else:
        print("No2 is Greater: ", No2)

if __name__ == "__main__":
    main()
