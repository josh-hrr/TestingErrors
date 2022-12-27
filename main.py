try:
  a, b = [int(x) for x in input("Enter two numbers: ").split()]
  c = a / b
except ZeroDivisionError:
  print("Division by zero is not allowed")

print("code after exception execution")

#reading a file

myFile = open("myfile.txt", "w")  
print("start typing... ") 
writeThis = "" 
while writeThis != "#":
  writeThis = input("enter an input: ")
  myFile.write(writeThis + "\n") 
myFile.close()

myFile = open("myfile.txt", "r")  
print(myFile.read()) 
myFile.close()