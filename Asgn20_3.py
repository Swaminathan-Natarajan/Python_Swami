import threading
import time

def ExtractEven(l):
    sum = 0
    for i in l:
        if i % 2 == 0:
            print("even number from list are :", i)
            sum = sum + i
    print("Sum of even:", sum)

def ExtractOdd(No):
    sum =0
    for i in No:
        if i % 2 != 0:
            print(" odd number from list are :", i)
            sum = sum + i
    print("Sum of odd is:", sum)


def main():
    Num = int(input("Enter a number:"))
    list1 = []
    for i in range(Num):
        Val = int(input(f"Enter {i} number :"))
        list1.append(Val)

    start_time = time.time()
    t1 = threading.Thread(target=ExtractEven,args=(list1,))
    
    t2 = threading.Thread(target=ExtractOdd, args=(list1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Total time taken for execution is:", end_time - start_time)

if __name__ == "__main__":
    main()