#welcome akhi
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through the list of numbers
for number in numbers:
    # Boolean condition to check if the number is even
    is_even = (number % 2 == 0)
    
    # Output the result using the Boolean variable
    if is_even:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
