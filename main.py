"""
Use a for loop to write a program that takes from the user 10 integers, adds them and prints the sum. 
"""
sum = 0
for i in range(10):
  userInt = int(input("Give me integers and I will give you the sum "))
  sum += userInt
print(sum)