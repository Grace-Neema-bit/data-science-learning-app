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

