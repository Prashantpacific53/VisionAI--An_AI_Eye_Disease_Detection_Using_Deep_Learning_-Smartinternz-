# Assignment No - 2

Use Methods of Python Datatypes (Objects) int, float, complex, list, tuple, str, set, dict, bool

# AI-ML Assignment 2: **Exploring Python Data Types & Methods**
**Author:** Prashant Kumar

# 🚀 Why Data Types Matter?
Imagine you are building an AI system that predicts health risks based on medical records. The data could include:

- Age (int): Whole numbers like **25, 45, 60**

- BMI (float): Decimal values like **24.5, 30.2**

- Symptoms (list): A collection of conditions like **['fever', 'cough', 'fatigue']**

Medical History (dict): Key-value pairs like **{'diabetes': True, 'hypertension': False}**
Each piece of data has a specific type, and knowing how to manipulate these types is essential for AI models!

# 📌 Python Data Types & Their Methods

🔢 **Numeric Types (int, float, complex)**

- Python has three main number types:

1️⃣ Integers (int) – Whole numbers like **100, -20, 0**

2️⃣ Floating-Point (float) – Decimal numbers like **3.14, 2.718**

3️⃣ Complex Numbers (complex) – Numbers with a real and imaginary part **(3 + 4j)**

# 🔍 Useful Methods for Numbers

python code is:
```
x = 10

y = 3.75

z = complex(4, 5)  # 4 + 5j

print(x.bit_length())   # Number of bits used to store 'x'

print(y.is_integer())   # False, since 3.75 is not an integer

print(z.conjugate())    # (4-5j), complex number conjugate
```
# 📜 Text Type (str)
Strings store text and are widely used in NLP, chatbots, and AI-driven assistants.

python code is:
```
text = "Artificial Intelligence"

#Methods to manipulate strings

print(text.upper())      # 'ARTIFICIAL INTELLIGENCE'

print(text.lower())      # 'artificial intelligence'

print(text.split())      # ['Artificial', 'Intelligence']

print(text.replace("Artificial", "Machine"))  # 'Machine Intelligence'
```
# 📦 Sequence Types (list, tuple)
Lists and tuples store **multiple values** and are useful for handling datasets.

✅ Lists (Mutable)

Lists allow modification (add, remove, update elements).

python code is:
```
symptoms = ["fever", "cough", "fatigue"]

symptoms.append("headache")  # Add new symptom

print(symptoms)  # ['fever', 'cough', 'fatigue', 'headache']
```
# 🔒 Tuples (Immutable)
Tuples are like lists but **cannot be modified** (useful for fixed data).

python code is: 
```
blood_groups = ("A", "B", "AB", "O")

print(blood_groups.count("A"))  # Counts occurrences of 'A'
```
# 🎯 Set Type (set)
Sets store **unique** values (useful for removing duplicates).

python code is:
```
diseases = {"Diabetes", "Hypertension", "Diabetes"}

print(diseases)  # {'Diabetes', 'Hypertension'}  (duplicates removed)
```
# 📑 Dictionary Type (dict)
Dictionaries store **key-value pairs**, like medical records.

python code is: 
```
patient = {

    "name": "John Doe",
    
    "age": 45,
    
    "diabetes": True
    
}

print(patient.keys())    # dict_keys(['name', 'age', 'diabetes'])

print(patient.values())  # dict_values(['John Doe', 45, True])

print(patient.get("age")) # 45
```
# 🔍 Boolean Type (bool)
Booleans store **True/False values**, useful in AI for decision-making.

python code is:
```
is_diabetic = True

print(is_diabetic)  # True

print(type(is_diabetic))  # <class 'bool'>
```
# Input:
```
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
```
# Output:
```
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
# 📌 Explanation of the Output:

Numeric Types
- Shows integer value and bit length.

- Checks if the float value is a whole number.

- Displays a complex number and its conjugate.

String Operations
- Converts text to uppercase/lowercase.
- Splits text into words.
- Replaces a word in the string.

Lists & Tuples
- Modifies a list by adding/removing items.
- Tuples remain unchanged, and we count elements.

Set Operations
- Demonstrates unique elements (removes duplicates).

Dictionary Operations
- Retrieves keys, values, and specific items.

Boolean Example
- Displays boolean value and its type.

Final Confirmation
- A success message confirms everything runs correctly.


# 💡 Summary
Python’s data types help **store, organize, and manipulate data** efficiently.

Knowing their methods allows us to **clean, process, and analyze data** before feeding it into AI models. 🚀
