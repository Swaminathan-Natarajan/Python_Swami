import hashlib #module to use md5 for checksum algorithm
import os
import sys


def CalculateCheckSum(FileName):
	
	print("FileName in CalculateCheckSum is:", FileName)
	fobj = open(FileName,"rb")
	
	hobj = hashlib.md5()
	
	Buffer = fobj.read(1000)

	while(len(Buffer) > 0):
		hobj.update(Buffer)
		Buffer = fobj.read(1024)
	
	fobj.close()
	
	return hobj.hexdigest()	


			
	
def GetFile(DirName, File1):

	for root, subroot, file in os.walk(DirName):
		for fname in file:
			if File1 in fname:
				fname = os.path.join(root, File1)

				return fname
	return None

			

def main():

	if(len(sys.argv) != 3 ):
		print("Invalid number of args")
		return
    	    
	currentDir = os.getcwd()
	print("Current Dir is :", currentDir)
	Ret1 = GetFile(currentDir, sys.argv[1])
	print("Ret1 is",Ret1)
	Ret2 = GetFile(currentDir, sys.argv[2])
	print("Ret2 is",Ret2)

	Value1 = CalculateCheckSum(Ret1)
	print("Value1 is",Value1)
	Value2 = CalculateCheckSum(Ret2)
	print("Value2 is",Value2)
	if Value1 == Value2:
		print("Success")
	else:
		print("Failure")
	

if __name__ == "__main__":
	main()