
StrLen = lambda String: len(String)>5

def main():
    Arr = ["Jay","Ganesh","Rama","Krishna","Swaminathan"]

    Res = list(filter(StrLen,Arr))

    print("Strings length greater than 5 :", Res)


if __name__ == "__main__":
    main()