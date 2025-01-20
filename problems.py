#Print the elements of the following list using for loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


for num in numbers:
    print(num)

#Search for a number in the given list [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

myList = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49


i = 0



for el in myList: 
    if el == x: 
        print("Found Index at: ", i)
        break
    i += 1

#Print numbers from 1 to 100 using range and for loop

for i in range(1, 101):
    print(i)


#Print numbers from 100 to 1 using range and for loop

for i in range(100, 1, -1):
    print(i)

# Print the multiplication table of a number n

userInput = int(input("Please enter a number: "))

for i in range(1, 11):
    print(f"Table of the numbers: {userInput} X {i}  ", userInput * i)

# WAP to find the sum of the first n numbers using for loop

userInput = int(input("Please enter a number: "))

sum = 0

for i in range (1, userInput + 1):
    sum += i
print("Total sum: ", sum)

# WAP to find the factorial of the first n numbers

userInput = int(input("Please enter a number: "))

factorial = 1 

for i in range(1, userInput + 1):
    factorial *= i
print(f"Factorial of the given number: {userInput} is: ", factorial)

# WAP to find the sum of the first n numbers using while loop

n = 5

i = 0

sum = 0

while i <= n:
    
    sum += i
    
    i += 1
print("Sum of the number is", sum)
