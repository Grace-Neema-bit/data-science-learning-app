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
    st.subheader("📌 What is Data Science?")
    st.write("""Your notes here...""")

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

