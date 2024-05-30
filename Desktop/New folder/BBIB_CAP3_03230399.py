
#Tshewang Rigzen 
#Section "B"
#Student number: 03230399

# References 
# https://www.w3schools.com/python/default.asp

# SOLUTION 
# 483692

import os

def calculate_answer_v2(file_name):
    total_sum = 0
    file_path = os.path.join(os.getcwd(), file_name)
    
    # Open and read the file line by line
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            
            # Find the first and last digits in the line
            digits = [char for char in line if char.isdigit()]
            if len(digits) >= 2:
                first_digit = digits[0]
                last_digit = digits[-1]
                
                # Form the two-digit number and add it to the total sum
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
    
    return total_sum

file_name = '399.txt'
answer = calculate_answer_v2(file_name)
print("Your answer is:", answer)
