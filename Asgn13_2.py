PI = 3.14
def AreaCircle(No):
    Area = PI * No * No
    return Area

    

def main():
    print("Enter the radius of the circle :")
    rad = int(input())


    Res = AreaCircle(rad)

    print("Area of a Circle is", Res)
    


if __name__ == "__main__":
    main()