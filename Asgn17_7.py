
    
def main():
    print("Enter a number:")
    Num = int(input())
    
    for i in range(1,Num+1):
        for j in range(1,Num+1):
            if j<=i:
                print(i, end=" ")
            else:
                print(j, end=" ")
        print()



if __name__ == "__main__":
    main()