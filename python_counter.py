# Python code​​​​​​‌‌‌‌​‌‌​​‌​‌​‌​​​​‌​‌​‌‌​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    count = 0
    if which == "even":
        for n in numbers:
            num = n % 2
            if num == 0:
                count = count + 1 
        return count
    elif which == "odd":
        for n in numbers:
            num = n % 2
            if num != 0:
                count = count + 1 
        return count
    else:
        return -1

# This is how your code will be called.
# You can edit this code to try different testing cases.
numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

# ****** DO NOT CHANGE THIS CODE ******
result1 = count_numbers("even", numbers)
result2 = count_numbers("odd", numbers)
result3 = count_numbers("Blarg", numbers)
