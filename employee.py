def outer(a, b):
   
    def inner(a, b):
        return a + b
    
    
    sum_value = inner(a, b)
    
    
    result = sum_value + 5
    
   
    return result


result = outer(10, 20)
print(f"Result: {result}")  

# Generate list of all even numbers between 4 to 30
even_numbers = [num for num in range(4, 31) if num % 2 == 0]

print(f"\nEven numbers between 4 to 30: {even_numbers}")

# Alternative method using range with step
even_numbers_alt = list(range(4, 31, 2))
print(f"Even numbers (using range): {even_numbers_alt}")

