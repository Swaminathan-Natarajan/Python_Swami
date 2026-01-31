import threading
import time

def displayEven(No):
    for i in range(No+1):
        if i % 2 == 0:
            print(" even number is :", i)

def displayOdd(No):
    for i in range(No+1):
        if i % 2 != 0:
            print(" odd number is :", i)


def main():
    start_time = time.time()
    t1 = threading.Thread(target=displayEven,args=(20,))
    
    t2 = threading.Thread(target=displayOdd, args=(20,))

    t1.start()
    t2.start()

    end_time = time.time()

    print("Total time taken for execution is:", end_time - start_time)

if __name__ == "__main__":
    main()