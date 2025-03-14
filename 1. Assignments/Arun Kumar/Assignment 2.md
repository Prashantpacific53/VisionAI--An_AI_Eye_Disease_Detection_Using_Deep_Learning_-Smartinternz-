
# Assignment No - 2

Exploring Python's Built-in Data Structures and Their Functionalities

# 🚀 Understanding Python Data Structures
Python provides a variety of built-in data structures that are crucial for handling and processing data efficiently. Let's explore them one by one with practical examples.

# 🔢 Numeric Data Types
Python supports three main numeric types:
- **Integer (int)**: Whole numbers such as 42, -17, 0.
- **Floating-Point (float)**: Decimal numbers like 3.14, -0.001.
- **Complex Numbers (complex)**: Numbers with real and imaginary parts (2 + 3j).

### Example Code:
```python
num_int = 50
num_float = 5.75
num_complex = complex(3, 4)  # 3 + 4j

print(num_int.bit_length())   # Number of bits required
print(num_float.as_integer_ratio())  # Float as a fraction
print(num_complex.conjugate())  # Complex conjugate
```

# 📜 Text Handling with Strings
Strings are sequences of characters used for textual data.

### Example Code:
```python
message = "Data Science with Python"
print(message.capitalize())  # Capitalize the first letter
print(message.swapcase())  # Swap uppercase and lowercase
print(message.count("a"))  # Count occurrences of 'a'
```

# 📦 Lists & Tuples
Lists are mutable sequences, whereas tuples are immutable.

### Example Code:
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an element
print(fruits)

days = ("Monday", "Tuesday", "Wednesday")
print(days.index("Tuesday"))  # Get index of an element
```

# 🎯 Working with Sets
Sets store unique elements and allow set operations.

### Example Code:
```python
unique_numbers = {1, 2, 2, 3, 4, 4}
print(unique_numbers)  # Duplicates removed
unique_numbers.add(5)
print(unique_numbers)
```

# 📑 Dictionaries - Key-Value Pairs
Dictionaries store data in key-value pairs, allowing efficient lookups.

### Example Code:
```python
student_info = {"name": "Alice", "age": 22, "major": "CS"}
print(student_info.keys())  # Retrieve keys
print(student_info.values())  # Retrieve values
print(student_info.get("age"))  # Retrieve specific value
```

# 🔍 Boolean Data Type
Booleans represent `True` or `False` values and are widely used in conditional statements.

### Example Code:
```python
is_active = False
print(is_active)
print(type(is_active))

# INPUT

# 📌 AI-ML Assignment 2: Python Data Types & Methods

# ===========================
# 🔢 Numeric Types (int, float, complex)
# ===========================

# Integer
x = 10
print("Integer:", x)
print("Bit length of x:", x.bit_length())  # Number of bits needed to store x

# Float
y = 3.75
print("\nFloat:", y)
print("Is y an integer?:", y.is_integer())  # Checks if y is a whole number

# Complex Number
z = complex(4, 5)  # 4 + 5j
print("\nComplex Number:", z)
print("Conjugate of z:", z.conjugate())  # Complex conjugate

# ===========================
# 📜 Text Type (str)
# ===========================

text = "Artificial Intelligence"
print("\nOriginal String:", text)
print("Uppercase:", text.upper())  # Convert to uppercase
print("Lowercase:", text.lower())  # Convert to lowercase
print("Split words:", text.split())  # Split string into list
print("Replace 'Artificial' with 'Machine':", text.replace("Artificial", "Machine"))

# ===========================
# 📦 Sequence Types (list, tuple)
# ===========================

# ✅ Lists (Mutable)
symptoms = ["fever", "cough", "fatigue"]
print("\nSymptoms List:", symptoms)
symptoms.append("headache")  # Add a new symptom
print("After Append:", symptoms)
symptoms.remove("cough")  # Remove an item
print("After Remove:", symptoms)

# 🔒 Tuples (Immutable)
blood_groups = ("A", "B", "AB", "O")
print("\nBlood Groups Tuple:", blood_groups)
print("Count of 'A' in tuple:", blood_groups.count("A"))

# ===========================
# 🎯 Set Type (set)
# ===========================

diseases = {"Diabetes", "Hypertension", "Diabetes"}  # Duplicate "Diabetes" is removed
print("\nDisease Set (Unique Values Only):", diseases)

# ===========================
# 📑 Dictionary Type (dict)
# ===========================

patient = {
    "name": "John Doe",
    "age": 45,
    "diabetes": True
}
print("\nPatient Dictionary:", patient)
print("Keys:", patient.keys())  # Get all keys
print("Values:", patient.values())  # Get all values
print("Patient Age:", patient.get("age"))  # Access value by key

# ===========================
# 🔍 Boolean Type (bool)
# ===========================

is_diabetic = True
print("\nBoolean Example:", is_diabetic)
print("Type of Boolean Variable:", type(is_diabetic))

# ===========================
# ✅ Conclusion
# ===========================

print("\n✅ All data types tested successfully!")


# Output 

Integer: 10
Bit length of x: 4

Float: 3.75
Is y an integer?: False

Complex Number: (4+5j)
Conjugate of z: (4-5j)

Original String: Artificial Intelligence
Uppercase: ARTIFICIAL INTELLIGENCE
Lowercase: artificial intelligence
Split words: ['Artificial', 'Intelligence']
Replace 'Artificial' with 'Machine': Machine Intelligence

Symptoms List: ['fever', 'cough', 'fatigue']
After Append: ['fever', 'cough', 'fatigue', 'headache']
After Remove: ['fever', 'fatigue', 'headache']

Blood Groups Tuple: ('A', 'B', 'AB', 'O')
Count of 'A' in tuple: 1

Disease Set (Unique Values Only): {'Hypertension', 'Diabetes'}

Patient Dictionary: {'name': 'John Doe', 'age': 45, 'diabetes': True}
Keys: dict_keys(['name', 'age', 'diabetes'])
Values: dict_values(['John Doe', 45, True])
Patient Age: 45

Boolean Example: True
Type of Boolean Variable: <class 'bool'>

✅ All data types tested successfully!
```

# 🔍 Summary
Python’s built-in data structures enable efficient handling and processing of various types of data. Mastering these structures is essential for problem-solving in AI, data science, and programming in general. 🚀
