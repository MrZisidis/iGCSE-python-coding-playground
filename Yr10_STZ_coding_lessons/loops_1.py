# number1 = int(input("Enter a number: "))
# number2 = int(input("Enter a number: "))
total=0
counter = 0

for i in range(1,4):
    number = int(input("Enter a number: "))
    counter = counter + 1
    total = total + number
    average = total / counter

print("the total is: ",total)
print("the average is: ", average)
