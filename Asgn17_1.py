import Arithmetic

def main():
    print("Enter the first number:")
    Num1 = int(input())

    print("Enter the Second number:")
    Num2 = int(input())

    Res1 = Arithmetic.Add(Num1,Num2)
    print("Addition : ", Res1)

    Res2 = Arithmetic.Sub(Num1, Num2)
    print("Sub :", Res2)

    Res3 = Arithmetic.Mult(Num1, Num2)
    print("Mult :", Res3)

    Res4 = Arithmetic.Div(Num1, Num2)
    print("Div :", Res4)

if __name__ == "__main__":
    main()