import threading
import time

def printNum(No):
    for i in range(No):
        print(i)

def reversePrint(No):
    for i in range(No,0,-1):
        print(i)


def main():
    start_time = time.time()
    t1 = threading.Thread(target=printNum,args=(50,))
    
    t2 = threading.Thread(target=reversePrint, args=(50,))

    t1.start()
    t1.join()
    t2.start()

    
    t2.join()

    end_time = time.time()

    print("Total time taken for execution is:", end_time - start_time)

if __name__ == "__main__":
    main()