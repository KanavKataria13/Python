## Question 1 

#print("""Twinkle, twinkle, little star,
#\tHow I wonder what you are!
#\t\tUp above the world so high,
#\t\tLike a diamond in the sky.
#Twinkle, twinkle, little star,
#\tHow I wonder what you are""")

## Question 2 

#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")
#print(last_name + " " + first_name)

## Question 3

#import math
#radius = float(input("Enter the radius of the circle: "))
#area = math.pi * (radius ** 2)
#print("The area of the circle is:", area)

## Question 4

#color_list = ["Red", "Green", "White", "Black"]
#print("First color:", color_list[0])
#print("Last color:", color_list[-1])

## Question 5

#n = int(input("Enter an integer: "))
#n1 = int(str(n))
#n2 = int(str(n) * 2)  # "nn"
#n3 = int(str(n) * 3)  # "nnn*

## Question 6

#numbers = input("Enter numbers separated by commas: ")
#number_list = numbers.split(",")
#number_tuple = tuple(number_list)
#print("List:", number_list)
#print("Tuple:", number_tuple)

## Question 7

#celsius = float(input("Enter temperature in Celsius: "))
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C is equal to {fahrenheit}°F")

## Question 8 

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print(f"Before swapping: a = {a}, b = {b}")
#a, b = b, a
#a += 1
#print(f"After swapping and incrementing 'a': a = {a}, b = {b}")

## Question 9 

#num = int(input("Enter a number: "))
#if num % 2 == 0:
 #   print(f"{num} is Even")
#else:
 #   print(f"{num} is Odd")
 
## Question 10

#year = int(input("Enter a year: "))
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print(f"{year} is a Leap Year")
#else:
 #   print(f"{year} is Not a Leap Year")

## Question 11

#import math
#x1 = float(input("Enter x1: "))
#y1 = float(input("Enter y1: "))
#x2 = float(input("Enter x2: "))
#y2 = float(input("Enter y2: "))
#distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#print(f"Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")

## Question 12

#angle1 = float(input("Enter first angle: "))
#angle2 = float(input("Enter second angle: "))
#angle3 = float(input("Enter third angle: "))
#if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
 #   print("The angles can form a triangle.")
#else:
#    print("The angles cannot form a triangle.")

## Question 13

#principal = float(input("Enter the principal amount: "))
#rate = float(input("Enter the annual interest rate (in %): "))
#time = float(input("Enter the time (in years): "))
#n = int(input("Enter the number of times interest is compounded per year: "))
#amount = principal * (1 + (rate / 100) / n) ** (n * time)
#compound_interest = amount - principal
#print(f"Compound Interest: {compound_interest}")
#print(f"Total Amount: {amount}")

## Question 14

#N = int(input("Enter a positive integer: "))
#if N <= 1:
 #   print(f"{N} is not a Prime Number")
#else:
 #   is_prime = True
  #  for i in range(2, int(N**0.5) + 1):  
   #     if N % i == 0:
    #        is_prime = False
     #       break
    
    #if is_prime:
    #    print(f"{N} is a Prime Number")
    #else:
     #   print(f"{N} is not a Prime Number")

## Question 15

#N = int(input("Enter a positive integer: "))
#sum_of_squares = (N * (N + 1) * (2 * N + 1)) // 6
#print(f"Sum of squares from 1² to {N}² is: {sum_of_squares}")
