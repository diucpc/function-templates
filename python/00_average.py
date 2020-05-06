# ⓒ DIU CPC
# Logic Series

# PROBLEM:
# The program takes the elements of the list one by one
# and displays the average of the elements of the list.

# Taking the how many value to store from user
value_counter = int(input("Enter the number of elements: "))

# Taking an empty list to store user's input
list_of_elements = []

# looping through the input number user has given
# and storing the value to list
for i in range(value_counter):        # this will loop 0 -> less than 'value_counter'
    value = int(input("Enter value: "))  # taking value from user
    list_of_elements.append(value)      # storing value to list

# calculating average
average = sum(list_of_elements) / value_counter

# do whatever you want with this average
