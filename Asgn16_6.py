def ChkPosNeg(Num):
    if Num > 0:
        return "Positive"
    elif Num < 0:
        return "Negative"
    else:
        return "Zero"




def main():
    print("Enter a Number:")
    Num = int(input())

    Res = ChkPosNeg(Num)

    if Res == "Positive":
        print("Positive")
    elif Res == "Negative":
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    main()