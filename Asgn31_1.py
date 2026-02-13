import sys
import os
import time




def DisplayFileExtensions(DirName, Extension):
    Border = "*"*55
    Timestamp = time.ctime()
    #LogFileName = "Assignment31-1%s.log"%(Timestamp)
    fobj = open("Marvellous","w")
    fobj.write(Border + "\n")
    fobj.write(f"----------Files with Extension {Extension} are ------------"+ "\n")

    if(os.path.isdir(DirName) == False):
        print("Not a Valid Dir")
        return
    
    if(os.path.exists(DirName) == False):
        print("Dir with this name does not exist")
        return
    
    FileExt = []
    #print("Extension passed is:", Extension)
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            #print(f"File names are: {fname}")
            #fname = os.path.join(FolderName, fname)
            #print("Value of f is:",fname)
            
            #print("Value of f is:",fname)
            print(os.path.splitext(fname)[1].lower())
            if os.path.splitext(fname)[1].lower() == Extension:
                #print("Inside if")
                FileExt.append(fname)
                print("FileExt is:", FileExt)
                
    

    fobj.write(Border+"\n")
    fobj.write("----------------- Automation Report Start -----------------"+ "\n")

    for i in FileExt:
        fobj.write(i+"\n")
    
    fobj.write("This log file is created at:" + Timestamp + "\n")
    fobj.write("----------------- Automation Report Ends -----------------"+ "\n")
    
    fobj.write(Border)
    fobj.close()		

def main():

    Border = "*"*50
    print(Border)
    print("------------Marvellous Directory Automation-----------------")
    print(Border)
    if(len(sys.argv) != 3 ):
        print("Invalid number of args, please pass 2 arguments: Directory name and File Extension")
        return


    DisplayFileExtensions(sys.argv[1], sys.argv[2])

    print(Border)
    print("------------Marvellous Directory Automation-----------")
    print(Border)


if __name__ == "__main__":
    main()