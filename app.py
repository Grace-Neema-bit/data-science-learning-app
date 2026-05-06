import streamlit as st

# MUST be first Streamlit command
st.set_page_config(page_title="Data Science Learning Hub", layout="wide")

# Title
st.title("📘 Data Science Learning Website")
st.write("Welcome 👋 Learn Data Science step by step.")

# Sidebar navigation
topic = st.sidebar.selectbox(
    "Choose a topic",
    [
        "🏠 Home",
        "💻 Setup: VS Code & Jupyter",
        "💻 Setup: VS Code & Jupyter"
        "📊 Introduction to Data Science",
        "🐍 Python Basics",
        "🐍 Python Intro Course",
        "⚙️ Python Functions Deep Dive",
        "🔁 Python Loops",
        "📈 Data Analysis",
        "🧠 Quiz"
    ]
)

# ---------------- HOME ----------------
if topic == "🏠 Home":
    st.header("Welcome 👋")
    st.write("""
    This platform will help you learn:
    - Python language
    - Pandas
    - SQL
    - Data analysis
    - Machine learning
    - Statistics
    - Natural language processing
    - Neural networks

    👉 Use the sidebar to start learning.
    """)
# ---------------- SETUP SECTION ----------------
elif topic == "💻 Setup: VS Code & Jupyter":
    st.header("💻 Setup: VS Code & Jupyter Notebook")

    st.subheader("🧑‍💻 What is VS Code?")
    st.write("""
    VS Code (Visual Studio Code) is a lightweight code editor used to write and run code.
    
    It supports:
    - Python programming
    - Extensions for data science
    - Debugging tools
    """)

    st.subheader("📥 How to Install VS Code")
    st.write("""
    1. Go to the official VS Code website  
    2. Download and install  
    3. Open VS Code after installation  
    """)

    st.subheader("⚙️ Install Python Extension")
    st.write("""
    1. Open VS Code  
    2. Click Extensions (left sidebar)  
    3. Search for "Python"  
    4. Install it  
    """)

    st.divider()

    st.subheader("📓 What is Jupyter Notebook?")
    st.write("""
    Jupyter Notebook is an interactive environment where you can:
    - Write code
    - See outputs instantly
    - Add explanations (notes)
    """)

    st.subheader("📥 How to Install Jupyter")
    st.code("""
pip install notebook
""")

    st.subheader("▶️ How to Run Jupyter Notebook")
    st.code("""
jupyter notebook
""")

    st.write("This will open Jupyter in your browser.")

    st.subheader("💡 Why Beginners Use Jupyter")
    st.write("""
    - Easy to test code step-by-step  
    - Great for learning and experiments  
    - Combines code + explanation  
    """)

    st.subheader("🧠 Quick Check")

    tool = st.radio(
        "Which tool is used for interactive notebooks?",
        ["VS Code", "Jupyter Notebook", "Excel"]
    )

    if st.button("Check Setup Answer"):
        if tool == "Jupyter Notebook":
            st.success("Correct 🎉")
        else:
            st.error("Try again ❌")
    st.divider()

    # ---------------- GIT SECTION ----------------
    st.header("🔧 Git & Git Bash Setup")

    st.subheader("📌 What is Git?")
    st.write("""
    Git is a version control system that helps you:
    - Track changes in your code
    - Save versions of your project
    - Collaborate with others
    """)

    st.subheader("📌 What is Git Bash?")
    st.write("""
    Git Bash is a terminal that allows you to run Git commands 
    using a Linux-style interface on Windows.
    """)

    st.subheader("📥 How to Install Git & Git Bash")
    st.write("""
    1. Go to the official Git website  
    2. Download Git for Windows  
    3. Install it (Git Bash will be installed automatically)  
    """)

    st.subheader("⚙️ First-Time Git Setup")
    st.write("After installing, open Git Bash and run:")

    st.code("""
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
""")

    st.subheader("📂 Basic Git Commands")
    st.code("""
git init
git add .
git commit -m "First commit"
git status
""")

    st.write("""
    - `git init` → Start a new project  
    - `git add .` → Add files  
    - `git commit` → Save changes  
    - `git status` → Check project status  
    """)

    st.subheader("🌐 Connect to GitHub")
    st.code("""
git remote add origin https://github.com/your-username/repo-name.git
git push -u origin main
""")

    st.write("""
    This uploads your project to GitHub so it can be shared and deployed.
    """)

    st.subheader("🧠 Quick Check")

    git_q = st.radio(
        "What does Git help you do?",
        ["Cook food", "Track code changes", "Play games"]
    )

    if st.button("Check Git Answer"):
        if git_q == "Track code changes":
            st.success("Correct 🎉")
        else:
            st.error("Try again ❌")
# ---------------- INTRODUCTION ----------------
elif topic == "📊 Introduction to Data Science":
    st.header("📊 Introduction to Data Science")

    st.subheader("📌 What is Data Science?")
    st.write("""
    Data Science is the process of extracting meaningful insights from data 
    using a combination of:
    - Statistics
    - Programming
    - Machine Learning
    """)

    st.subheader("🎯 Why is Data Science Important?")
    st.write("""
    Data Science helps organizations:
    - Make better decisions
    - Predict future trends
    - Understand customer behavior
    """)

    st.subheader("🌍 Real-World Applications")
    st.write("""
    - Netflix recommends movies based on your preferences  
    - Banks detect fraudulent transactions  
    - Hospitals predict patient demand  
    """)

    st.subheader("🛠️ Tools Used in Data Science")
    st.write("""
    - Python  
    - Pandas  
    - Machine Learning libraries  
    """)

# ➕ ADD NEW SECTION
    st.subheader("📊 Types of Data")
    st.write("""
    There are different types of data:

    - Structured data (tables, databases)
    - Unstructured data (text, images)
    - Semi-structured data (JSON, XML)
    """)

# ➕ ADD NEW SECTION
    st.subheader("🔄 Data Science Workflow")
    st.write("""
    A typical data science workflow includes:

    1. Data collection  
    2. Data cleaning  
    3. Data analysis  
    4. Modeling  
    5. Deployment  
    """)

# ➕ ADD NEW SECTION
    st.subheader("👨‍💻 Roles in Data Science")
    st.write("""
    - Data Analyst → works with data insights  
    - Data Scientist → builds models  
    - Data Engineer → builds data pipelines  
    """)

    st.subheader("🧠 Quick Check")
    answer = st.radio(
        "Which of these is part of Data Science?",
        ["Cooking", "Statistics", "Driving"]
    )

    if st.button("Check Answer"):
        if answer == "Statistics":
            st.success("Correct 🎉")
        else:
            st.error("Try again ❌")

# ---------------- PYTHON BASICS ----------------
elif topic == "🐍 Python Basics":
    st.header("🐍 Python Basics")

    st.subheader("Variables")
    st.write("Variables store data values.")

    st.code("""
x = 10
y = 5
print(x + y)
""")

    st.subheader("Try it yourself")

    num = st.number_input("Enter a number", value=0)

    if st.button("Add 10"):
        st.success(f"Result: {num + 10}")

elif topic == "🐍 Python Intro Course":
    st.header("🐍 Introduction to Python for Data Science")
    st.write("Instructor: Data Science Technical Mentor")

    st.divider()

    # ---------------- LESSON OUTLINE ----------------
    st.subheader("📌 Lesson Outline")
    st.write("""
    - What is Python?
    - Why Python?
    - Python Installation
    - Python Syntax
    - Basic Data Types
    - Variables and Constants
    - Control Structures
    - Functions
    - Python Libraries
    - Hands-on Examples
    - Conclusion
    - Mini Exercises
    """)

    st.divider()

    # ---------------- WHAT IS PYTHON ----------------
    st.subheader("1. What is Python?")
    st.write("""
    Python is a high-level, easy-to-read programming language created by Guido van Rossum.

    It is widely used in:
    - Data Science
    - Artificial Intelligence
    - Automation
    """)

    st.subheader("2. Why Python?")
    st.write("""
    - Easy to learn and read  
    - Huge community support  
    - Powerful Data Science libraries  
    - Free and open-source  
    """)

    st.subheader("3. Python Installation")
    st.write("""
    Steps:
    1. Go to https://www.python.org/
    2. Download latest version
    3. Check "Add to PATH"
    4. Verify installation:
    """)

    st.code("python --version", language="bash")

    st.subheader("4. Python Syntax")
    st.code('print("Hello, world!")')

    st.subheader("5. Basic Data Types")
    st.write("""
    - Integer → 5  
    - Float → 5.7  
    - String → "hello"  
    - Boolean → True / False  
    """)

    st.subheader("6. Variables and Constants")
    st.code("""
name = "Alice"
age = 25
PI = 3.14
""")

    st.subheader("7. Control Structures")

    st.write("If Statement:")
    st.code("""
age = 18
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")
""")

    st.write("Loop Example:")
    st.code("""
for i in range(3):
    print("Hello", i)
""")

    st.subheader("8. Functions")
    st.code("""
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
""")

    st.subheader("9. Python Libraries")
    st.code("""
import pandas as pd
import numpy as np
""")

    st.subheader("10. Hands-on Examples")

    st.write("Basic Calculator")
    st.code("""
a = 10
b = 5

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
""")

    st.write("Check Even or Odd")
    st.code("""
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
""")

    st.subheader("11. Data Structures")

    st.write("Lists")
    st.code("""
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
""")

    st.write("Dictionaries")
    st.code("""
person = {"name": "Alice", "age": 25}
print(person["name"])
""")

    st.subheader("12. Comparison Operators")
    st.code("""
x = 10
y = 5
print(x > y and y < 3)
""")

    st.subheader("13. Python Built-in Methods")
    st.code("""
text = "hello"
print(text.upper())
print(len(text))

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
""")

    st.subheader("14. Conclusion")
    st.write("""
Python is:
- Simple
- Powerful
- Essential for Data Science careers
""")

    st.divider()

    # ---------------- MINI EXERCISES ----------------
    st.subheader("🧠 Mini Exercises")

    q1 = st.radio(
        "1. What is Python used for?",
        ["Cooking", "Data Science", "Driving"],
        key="py_q1"
    )

    q2 = st.radio(
        "2. What does a list use?",
        ["()", "[]", "{}"],
        key="py_q2"
    )

    q3 = st.radio(
        "3. What keyword defines a function?",
        ["def", "function", "fun"],
        key="py_q3"
    )

    if st.button("Submit Python Quiz"):
        score = 0

        if q1 == "Data Science":
            score += 1
        if q2 == "[]":
            score += 1
        if q3 == "def":
            score += 1

        st.success(f"You scored {score}/3 🎉")

elif topic == "⚙️ Python Functions Deep Dive":
    st.header("⚙️ Functions in Python")

    st.write("""
Functions are reusable blocks of code that perform specific tasks.
They help make code cleaner, reusable, and easier to manage.
""")

    st.divider()

    # ---------------- WHAT IS A FUNCTION ----------------
    st.subheader("📌 What is a Function in Python?")
    st.write("""
A function is a block of code that performs a specific task.

Why we use functions:
- Avoid repeating code
- Improve readability
- Break big problems into smaller parts
""")

    st.code("""
def add(a, b):
    return a + b

add(1, 2)
""")

    st.caption("👉 Single Responsibility Principle: each function should do ONE job")

    st.divider()

    # ---------------- BASIC FUNCTION ----------------
    st.subheader("🔹 Defining and Calling Functions")

    st.code("""
def greet():
    print("Hello, welcome to class!")

greet()
""")

    st.success("Hello, welcome to class!")

    st.divider()

    # ---------------- PARAMETERS ----------------
    st.subheader("📥 Functions with Parameters")

    st.code("""
def greet(name):
    print("Hello", name, "- welcome to class!")

greet("Alice")
greet("Bob")
""")

    st.write("Example Output:")
    st.success("Hello Alice - welcome to class!")
    st.success("Hello Bob - welcome to class!")

    st.code("""
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Tom", 20)
introduce("Alice", 25)
""")

    st.divider()

    # ---------------- RETURN VALUES ----------------
    st.subheader("🔄 Functions That Return Values")

    st.code("""
def add(x, y):
    return x + y

result = add(3, 5)
print(result)
""")

    st.success("Result: 8")

    st.divider()

    # ---------------- REAL WORLD EXAMPLE ----------------
    st.subheader("🧹 Real-Life Example: Data Cleaning")

    st.code("""
def clean_name(name):
    return name.strip().title()

names = [" alice ", "BOB", "   charLie"]
cleaned = [clean_name(n) for n in names]
print(cleaned)
""")

    st.success("['Alice', 'Bob', 'Charlie']")

    st.divider()

    # ---------------- LAMBDA FUNCTIONS ----------------
    st.subheader("⚡ Lambda Functions (Anonymous Functions)")

    st.write("""
Lambda functions are short functions used for quick operations.
""")

    st.code("""
square = lambda x: x * x
square(2)
""")

    st.success("4")

    st.code("""
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)
""")

    st.success("[1, 4, 9, 16]")

    st.code("""
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
""")

    st.success("[2, 4]")

    st.divider()

    # ---------------- QUIZ ----------------
    st.subheader("🧠 Quick Quiz")

    q1 = st.radio(
        "1. What is the main purpose of functions?",
        ["Store data", "Reuse code", "Design websites"],
        key="func_q1"
    )

    q2 = st.radio(
        "2. What keyword defines a function?",
        ["def", "function", "lambda"],
        key="func_q2"
    )

    q3 = st.radio(
        "3. What do lambda functions do?",
        ["Make coffee", "Short anonymous functions", "Install packages"],
        key="func_q3"
    )

    if st.button("Submit Function Quiz"):
        score = 0

        if q1 == "Reuse code":
            score += 1
        if q2 == "def":
            score += 1
        if q3 == "Short anonymous functions":
            score += 1

        st.success(f"You scored {score}/3 🎉")

elif topic == "🔁 Python Loops":
    st.header("🔁 Python Loops")

    st.write("""
Loops allow us to repeat a block of code multiple times.
They are essential for automation and data processing.
""")

    st.divider()

    # ---------------- WHAT ARE LOOPS ----------------
    st.subheader("📌 What Are Loops?")
    st.write("""
A loop repeats a set of instructions.

Python has two main types:
- for loops
- while loops
""")

    st.divider()

    # ---------------- FOR LOOP ----------------
    st.subheader("🔹 The for Loop")

    st.code("""
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
""")

    st.success("apple\nbanana\ncherry")

    st.divider()

    # ---------------- WHILE LOOP ----------------
    st.subheader("🔹 The while Loop")

    st.code("""
count = 1

while count <= 3:
    print("Count is:", count)
    count += 1
""")

    st.success("Count is: 1\nCount is: 2\nCount is: 3")

    st.divider()

    # ---------------- LOOP CONTROL ----------------
    st.subheader("⚙️ Loop Control Statements")

    st.write("Break statement:")

    st.code("""
for i in range(5):
    if i == 3:
        break
    print(i)
""")

    st.success("0\n1\n2")

    st.write("Continue statement:")

    st.code("""
for i in range(5):
    if i == 3:
        continue
    print(i)
""")

    st.success("0\n1\n2\n4")

    st.write("Else with loop:")

    st.code("""
for i in range(5):
    print(i)
else:
    print("Loop completed without break")
""")

    st.success("0\n1\n2\n3\n4\nLoop completed without break")

    st.divider()

    # ---------------- NESTED LOOPS ----------------
    st.subheader("🔁 Nested Loops")

    st.code("""
for day in ["Mon", "Tue"]:
    for subject in ["Math", "English"]:
        print(day, subject)
""")

    st.success("Mon Math\nMon English\nTue Math\nTue English")

    st.divider()

    # ---------------- LOOP EXAMPLE ----------------
    st.subheader("➕ Loop Example: Sum of Numbers")

    st.code("""
total = 0

for i in range(1, 6):
    total += i

print("Total:", total)
""")

    st.success("Total: 15")

    st.divider()

    # ---------------- BEST PRACTICES ----------------
    st.subheader("💡 Best Practices")
    st.write("""
- Keep loops simple and readable  
- Avoid deeply nested loops  
- Use break/continue carefully  
- Ensure while loops eventually stop  
""")

    st.divider()

    # ---------------- MINI QUIZ ----------------
    st.subheader("🧠 Mini Exercises")

    q1 = st.radio(
        "1. Which loop is best when you know number of iterations?",
        ["while loop", "for loop", "if statement"],
        key="loop_q1"
    )

    q2 = st.radio(
        "2. What does 'break' do?",
        ["Stops loop", "Skips iteration", "Repeats loop"],
        key="loop_q2"
    )

    q3 = st.radio(
        "3. What does 'continue' do?",
        ["Ends program", "Skips current iteration", "Deletes loop"],
        key="loop_q3"
    )

    if st.button("Submit Loop Quiz"):
        score = 0

        if q1 == "for loop":
            score += 1
        if q2 == "Stops loop":
            score += 1
        if q3 == "Skips current iteration":
            score += 1

        st.success(f"You scored {score}/3 🎉")
# ---------------- DATA ANALYSIS ----------------
elif topic == "📈 Data Analysis":
    st.header("📈 Data Analysis with Pandas")

    st.write("Pandas helps you analyze data.")

    st.code("""
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
""")

    st.write("This loads and shows the first rows of a dataset.")

# ---------------- QUIZ ----------------
elif topic == "🧠 Quiz":
    st.header("🧠 Quick Quiz")

    q1 = st.radio(
        "What is Python used for?",
        ["Gaming only", "Data analysis", "Cooking"]
    )

    if st.button("Submit Answer"):
        if q1 == "Data analysis":
            st.success("Correct 🎉")
        else:
            st.error("Try again ❌")

