# List of Numbers Operations

# a) Creating a List of Numbers
numbers = [10, 20, 30, 40, 50]
print("Created list:", numbers)

# b) Accessing List Elements
print("\nAccessing Elements:")
print("First number:", numbers[0])  # First element
print("Last number:", numbers[-1])  # Last element
print("Second and third numbers:", numbers[1:3])  # Slice

# c) Updating List Elements
print("\nUpdating Elements:")
numbers[2] = 35  # Change third element
print("Updated list:", numbers)

numbers.append(60)  # Add to end of list
print("After adding:", numbers)

# d) Deleting List Elements
print("\nDeleting Elements:")
numbers.remove(40)  # Remove by value
print("After removing 40:", numbers)

del numbers[1]  # Remove by index
print("After deleting second element:", numbers)

# Bonus: Additional number list operations
print("\nBonus Operations:")
print("List length:", len(numbers))
print("Sum of numbers:", sum(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
