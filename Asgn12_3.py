import Marvellous

    

def main():
    print("Enter the first number :")
    no1 = int(input())

    print("Enter the second number :")
    no2 = int(input())

    Res1 = Marvellous.Add(no1, no2)
    Res2 = Marvellous.Sub(no1, no2)
    Res3 = Marvellous.Mult(no1, no2)
    Res4 = Marvellous.Div(no1, no2)

    print("Addition is:", Res1)
    print("Substraction is:", Res2)
    print("Multiplication is:", Res3)
    print("Division is:", Res4)


if __name__ == "__main__":
    main()