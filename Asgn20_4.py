import threading
import time

def lowercase(str):
    upper_ctr = 0
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            upper_ctr += 1
    print("Lower case count is:", upper_ctr)

def uppercase(str):
    upper_ctr = 0
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            upper_ctr += 1
    print("Upper case count is:", upper_ctr)

def digitscase(str):
    upper_ctr = 0
    for i in range(len(str)):
        if str[i] >= '0' and str[i] <= '9':
            upper_ctr += 1
    print("Digits count is:", upper_ctr)


def main():
    String = input("Enter a String:")
    

    start_time = time.time()
    small = threading.Thread(target=lowercase,args=(String,))
    
    capital = threading.Thread(target=uppercase, args=(String,))

    digits = threading.Thread(target=digitscase, args=(String,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    end_time = time.time()

    print("Total time taken for execution is:", end_time - start_time)

if __name__ == "__main__":
    main()