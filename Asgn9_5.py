def Divisible(No1):
    if No1%3 == 0 and No1%5 ==0:
        return True
    
        

def main():
    print("Enter the first number :")
    No1 = int(input())
    
    Res = Divisible(No1)

    if Res == True:
        print("Number Entered is Divisible by 3 and 5:", No1)
    else:
        print("Number Entered is not divisible by 3 and 5:", No1)
        

if __name__ == "__main__":
    main()
