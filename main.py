try:
  a, b = [int(x) for x in input("Enter two numbers: ").split()]
  c = a / b
except ZeroDivisionError:
  print("Division by zero is not allowed")

print("code after exception execution")