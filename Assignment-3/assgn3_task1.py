def factorial_loop(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
def factorial_recursive(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

num = int(input("Enter a number: "))

print(f"Factorial of {num} (using loop):", factorial_loop(num))
print(f"Factorial of {num} (using recursion):", factorial_recursive(num))
