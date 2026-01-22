def Square(No1):
    return No1**2
        

def main():
    print("Enter the first number :")
    No1 = int(input())
    
    Res = Square(No1)
    
    print("Square of number entered is :", Res)
    

if __name__ == "__main__":
    main()
