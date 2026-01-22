def AreaRectangle(No1, No2):
    Area = No1 * No2
    return Area

    

def main():
    print("Enter the length :")
    len = int(input())

    print("Enter the breadth :")
    breadth = int(input())

    Res = AreaRectangle(len, breadth)

    print("Area of a Rectangle is", Res)
    


if __name__ == "__main__":
    main()