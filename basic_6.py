def transform_string(input_str):
    transformed_str = ''
    
    for i,char in enumerate(input_str):

        transformed_char = chr(ord(char) - i)
        transformed_str += transformed_char
        # print(char)

    
    return transformed_str

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and display the transformed string
result = transform_string(user_input)
print("Transformed string:", result)
