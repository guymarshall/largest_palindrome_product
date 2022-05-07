def reverse_string(input):
    return input[::-1]

def is_palindrome(number):
    number_as_string = str(number)
    return number_as_string == str(number)[::-1]

def main():
    user_input = int(input("Enter a number of digits: "))
    max_number = (10 ** user_input) - 1
    largest_palindrome = 0
    product = 1

    for i in range(max_number + 1):
        for j in range(max_number):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
            
        
    print(f"Maximum palindrome product for {user_input} digits is {largest_palindrome}")

if __name__ == "__main__":
    main()