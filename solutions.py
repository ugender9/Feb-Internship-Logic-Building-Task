"""Feb Internship Logic Building Task - Solutions
Complete Python solutions for 10 programming problems
"""

print("=" * 60)
print("PROBLEM 1: Unique Words in a Sentence")
print("=" * 60)

# Problem 1: Unique Words in a Sentence
sentence = "python is easy and python is powerful"
words = sentence.split()
unique_words = set(words)
print(f"Input: {sentence}")
print(f"Unique words count: {len(unique_words)}")
print(f"Unique words: {unique_words}")
print()

print("=" * 60)
print("PROBLEM 2: Highest Salary from Employee Data")
print("=" * 60)

# Problem 2: Highest Salary
employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}
max_salary = max(employees.values())
max_employee = [name for name, salary in employees.items() if salary == max_salary][0]
print(f"Employees: {employees}")
print(f"Highest Salary: {max_employee} - {max_salary}")
print()

print("=" * 60)
print("PROBLEM 3: Find Maximum and Minimum Values")
print("=" * 60)

# Problem 3: Find Maximum and Minimum
numbers = [45, 22, 89, 10, 66]
max_val = max(numbers)
min_val = min(numbers)
print(f"List: {numbers}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")
print()

print("=" * 60)
print("PROBLEM 4: Count Products Above a Price Threshold")
print("=" * 60)

# Problem 4: Count Products Above Price
prices = [150, 200, 75, 300, 120, 250]
threshold = 200
count = sum(1 for price in prices if price > threshold)
print(f"Prices: {prices}")
print(f"Threshold: {threshold}")
print(f"Count of products above threshold: {count}")
print()

print("=" * 60)
print("PROBLEM 5: Calculate Attendance Percentage")
print("=" * 60)

# Problem 5: Attendance Percentage
classes_attended = 75
total_classes = 100
attendance_percentage = (classes_attended / total_classes) * 100
print(f"Classes attended: {classes_attended}")
print(f"Total classes: {total_classes}")
print(f"Attendance Percentage: {attendance_percentage}%")
print()

print("=" * 60)
print("PROBLEM 6: Remove Duplicate Phone Numbers")
print("=" * 60)

# Problem 6: Remove Duplicates
phone_numbers = ["9876543210", "1234567890", "9876543210", "5555555555", "1234567890"]
unique_phones = list(set(phone_numbers))
print(f"Original: {phone_numbers}")
print(f"Unique: {unique_phones}")
print()

print("=" * 60)
print("PROBLEM 7: Count Character Frequency")
print("=" * 60)

# Problem 7: Character Frequency
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(f"Text: {text}")
print(f"Character Frequency: {freq}")
print()

print("=" * 60)
print("PROBLEM 8: Convert List to Tuple")
print("=" * 60)

# Problem 8: List to Tuple
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print()

print("=" * 60)
print("PROBLEM 9: Check if a Key Exists in a Dictionary")
print("=" * 60)

# Problem 9: Check Key Existence
employee_data = {"name": "John", "age": 30, "department": "IT"}
key_to_check = "name"
if key_to_check in employee_data:
    print(f"Employee exists")
else:
    print(f"Employee does not exist")
print()

print("=" * 60)
print("PROBLEM 10: Calculate Average Marks")
print("=" * 60)

# Problem 10: Average Marks
marks = [85, 90, 75, 80, 70]
average = sum(marks) / len(marks)
print(f"Marks: {marks}")
print(f"Average Marks: {average}")
print()

print("=" * 60)
print("All problems completed successfully!")
print("=" * 60)
