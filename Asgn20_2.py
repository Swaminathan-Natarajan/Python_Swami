import threading
import time

def displayEvenFactors(No):
    sum = 0
    fact = []
    for i in range(1,No):
        if No % i == 0:
            fact.append(i)
    print("Factors of num :", fact)
    for i in fact:
        if i % 2 == 0:
            sum = sum + i

    print("Even Sum is :", sum)

def displayOddFactors(No):
    sum = 0
    fact = []
    for i in range(1,No):
        if No % i == 0:
            fact.append(i)
    print("Factors of num :", fact)
    for i in fact:
        if i % 2 != 0:
            sum = sum + i

    print("Odd Sum is :", sum)


def main():
    Num = int(input("Enter a integer:"))
    start_time = time.time()
    t1 = threading.Thread(target=displayEvenFactors,args=(Num,))
    
    t2 = threading.Thread(target=displayOddFactors, args=(Num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time = time.time()

    print("Total time taken for execution is:", end_time - start_time)
    print("Exit from Main...")

if __name__ == "__main__":
    main()