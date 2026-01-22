

def EvenCount(A):
    return A%2==0



def main():
    Arr = [3,2,4,5,10,22, 43]

    Res = list(filter(EvenCount,Arr))
    
    print("Count of Even numbers :", len(Res))


if __name__ == "__main__":
    main()