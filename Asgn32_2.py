import hashlib #module to use md5 for checksum algorithm
import os
import sys
import time

def CalculateCheckSum(FileName):
	
	fobj = open(FileName,"rb")
	
	hobj = hashlib.md5()
	
	Buffer = fobj.read(1000)

	while(len(Buffer) > 0):
		hobj.update(Buffer)
		Buffer = fobj.read(1024)
	
	fobj.close()
	
	return hobj.hexdigest()	

def ListDuplicateFiles(DirectoryName):
	Border = "*"*55
	Timestamp = time.ctime()
	fobj = open("Log.txt","w")
	fobj.write(Border + "\n")
	
	
	Ret = False
	Ret = os.path.exists(DirectoryName)
	
	if(Ret == False):
		print("There is no such Dir")
		return

	Ret = os.path.isdir(DirectoryName)
	if(Ret == False):
		print("It is not a Dir")
		return	
	
	Duplicate = {}
	
	for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
		for fName in FileName:
			fName = os.path.join(FolderName,fName)
			CheckSum = CalculateCheckSum(fName)

			if CheckSum in Duplicate:
				Duplicate[CheckSum].append(fName)
			else:
				Duplicate[CheckSum] = [fName]
			
			
					
	#print("Duplicate mapping result is:", Duplicate, "\n")

	Result = []
	for i in Duplicate.values():
		if len(i)>1:
			Result.append(i)

	FinalResult = []
	for val in Result:
		print("Value is:", val)
		for subVal in val:
			print("SubValue is :", subVal)
			FinalResult.append(subVal)
	#print("Result values are:", Result,"\n")
	fobj.write(f"Duplicate files in the given Directory {DirectoryName} are : {FinalResult} \n" )

	fobj.write(Border)
    

    	

			

def main():
	Border = "*"*50
	print(Border)
	print("------------Marvellous Directory Automation-----------------")
	print(Border)
	if(len(sys.argv) != 2 ):
		print("Invalid number of args")
		return

	ListDuplicateFiles(sys.argv[1])
	
	print(Border)
	print("------------Marvellous Directory Automation-----------")
	print(Border)

if __name__ == "__main__":
	main()