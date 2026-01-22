def table(No1):
    
    table_val = []
    for i in range(4,40+1,4):
        table_val.append(i)

    return table_val


def main():
    print("Enter the number:")
    No1 = int(input())

    Res = table(No1)

    print("Table of the number entered is :", Res)

if __name__ == "__main__":
    main()