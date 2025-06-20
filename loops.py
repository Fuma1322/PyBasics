# Loops

# for loop
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
    
numbers = [1,2,3,4]

for number in numbers:
    print(number)
    
# while loop

num = 1

while num <= 5:
    print(num)
    num += 1 #Increments the num by 1
    
    
# Loop Control statements

fruits = ["apple", "banana", "orange", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  #exits the loops when cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue  #skips cherry and moves the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass  #Placeholder, no action is needed for cherry
    print(fruit)

# while 
count = 0 

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  #exits the loops when 3 is reached
