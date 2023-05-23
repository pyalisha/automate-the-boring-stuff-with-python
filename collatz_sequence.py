# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.

def collatz(number):
    try:
        if number!=1:
            if number%2==0:
                return [number] + collatz(number//2)
            else:
                return [number] + collatz(number*3 + 1)
        else:
            return [1]
    except TypeError:
        print("Enter an integer value only")
    
   
print(collatz(1))
# print(collatz('puppy'))
