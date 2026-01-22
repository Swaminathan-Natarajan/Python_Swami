def Cube(No1):
    return No1**3
        

def main():
    print("Enter the first number :")
    No1 = int(input())
    
    Res = Cube(No1)
    
    print("Cube of number entered is :", Res)
    

if __name__ == "__main__":
    main()
