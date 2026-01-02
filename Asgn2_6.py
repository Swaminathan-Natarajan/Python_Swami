#Accept 2 int inputs and write prog for addtion, substraction, multiplication and division
print("Enter the first num :")
num1 = int(input())
print("Enter the second num :")
num2 = int(input())
add = num1 + num2
print("Addition is :", add)

sub = num1 - num2
print("Substraction is : ", sub)

mult = num1 * num2
print("multiplication is : ", mult)

if num1 > num2 and num2 != 0 :
    div = num1/num2
    print("Division is : ", div)

