# Replace all Extension1 by Extension2
import sys
import os
import time




def CopyFiles(DirName1, DirName2):
    Border = "*"*55
    Timestamp = time.ctime()
    #LogFileName = "Assignment31-1%s.log"%(Timestamp)
    fobj = open("Marvellous2","w")
    fobj.write(Border + "\n")
    #fobj.write(f"----------Files with Extension Replacement from {Extension1} By {Extension2} ------------"+ "\n")


    if(os.path.isdir(DirName1) == False):
        print("Not a Valid Dir")
        return
    
    if(os.path.exists(DirName1) == False):
        print("Dir with this name does not exist")
        return
    
    if(os.path.exists(DirName2) == False):
        os.makedirs(DirName2)
    
    fobj1 = None
    fobj2 = None

    for FolderName, SubFolderName, FileName in os.walk(DirName1):
        for fname in FileName:
            
            path1 = os.path.join(FolderName, fname)
            path2 = os.path.join(DirName2, fname)

            print("Path1 is:", path1)
            print("path 2 is:",path2)

            if os.path.isfile(path1):
                fobj1 = open(path1, "rb")
                fobj2 = open(path2,"wb")
                fobj2.write(fobj1.read())

                print(f"Copied: {fobj1} -> {fobj2}")
                fobj.write(f"Copied: {fobj1} -> {fobj2}"+"\n")      

    
    

    fobj.write(Border+"\n")
    fobj.write("----------------- Automation Report Start -----------------"+ "\n")

    
    
    
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

   

    CopyFiles(sys.argv[1], sys.argv[2])

    print(Border)
    print("------------Marvellous Directory Automation-----------")
    print(Border)


if __name__ == "__main__":
    main()