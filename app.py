import streamlit as st

st.title("📘 Data Science Learning Website")

st.write("Welcome to your learning platform!")
import streamlit as st

st.set_page_config(page_title="Data Science Learning Hub", layout="wide")

# Title
st.title("📘 Data Science Learning Website")
st.write("Welcome 👋 Learn Data Science step by step.")

# Sidebar navigation
topic = st.sidebar.selectbox(
    "Choose a topic",
    ["🏠 Home", "📊 What is Data Science", "🐍 Python Basics", "📈 Data Analysis", "🧠 Quiz"]
)

# ---------------- HOME ----------------
if topic == "🏠 Home":
    st.header("Welcome")
    st.write("""
    This platform will help you learn:
    - Python basics
    - Data analysis
    - Machine learning foundations
    
    👉 Use the sidebar to start learning.
    """)

# ---------------- DATA SCIENCE INTRO ----------------
elif topic == "📊 What is Data Science":
    st.header("📊 What is Data Science?")
    
    st.write("""
    Data Science is the process of extracting insights from data using:
    - Statistics
    - Programming
    - Machine Learning
    """)

    st.subheader("Real-world examples:")
    st.write("""
    - Netflix recommending movies  
    - Banks detecting fraud  
    - Hospitals predicting patient demand  
    """)

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