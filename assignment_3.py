#que4
'''
sentence=input("enter the string")
new=sentence.replace("the","?")
print(new)
'''
#que5
'''
# Accepting input string from the user
input_string = input("Enter a string: ")

# Initializing counters
lower_count = 0
upper_count = 0
has_numeric = False

# Looping through each character in the string
for char in input_string:
    if char.islower():
        lower_count=lower_count+1
    elif char.isupper():
        upper_count=upper_count+1
    elif char.isdigit():
        has_numeric=True
# Printing the results
print(f"Number of lowercase letters: {lower_count}")
print(f"Number of uppercase letters: {upper_count}")
print(f"Are there numeric values? {'Yes' if has_numeric else 'No'}")
'''
#que1

# Accepting the input string
input_string = input("Enter a string: ")

# Checking if the string is in upper case or lower case
if input_string.isupper():
    print("The string is in upper case.")
elif input_string.islower():
    print("The string is in lower case.")
else:
    print("The string contains both upper and lower case letters.")

# Swapping the case and printing the result
swapped_string = input_string.swapcase()
print(f"Swapped case string: {swapped_string}")

#que7
# Accepting the input string
input_string = input("Enter a string: ")

# Check if the string starts with 'S'
if input_string.startswith('S'):
    # Reverse the string
    reversed_string = input_string[::-1]
    print(f"Reversed string: {reversed_string}")
else:
    print("The string does not start with 'S'.")

