# Initialize flag variables to track if maximum and minimum have been set
max_set = False
min_set = False

# Initialize variables to store maximum and minimum values
max_value = None
min_value = None

# Prompt the user to enter numbers
while True:
    num = input("Enter a number (or type 'done' to finish): ")
    if num == 'done':
        break  # Exit the loop if user types 'done'
    num = int(num)
    # If max_value is not set or the current number is greater than max_value, update max_value
    if not max_set or num > max_value:
        max_value = num
        max_set = True
    # If min_value is not set or the current number is smaller than min_value, update min_value
    if not max_set or num < min_value:
        min_value = num
        min_set = True

# Print the maximum and minimum values
if max_set:
    print("Maximum value:", max_value)
else:
    print("No maximum value found.")
if min_set:
    print("Minimum value:", min_value)
else:
    print("No minimum value found.")
