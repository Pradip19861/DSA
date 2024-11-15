def ispalindrome(n):
    n_str = str(n)  # Convert number to string for easy reversal check
    if n_str == n_str[::-1]:  # Check if it's a palindrome
        return n  # Return the palindrome number
    else:
        # Add the number and its reverse, and call ispalindrome on the result
        reversed_n = int(n_str[::-1])
        return ispalindrome(n + reversed_n)

print(ispalindrome(195))  # Example use