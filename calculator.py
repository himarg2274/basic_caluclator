import streamlit as st

st.set_page_config(page_title="Basic Calculator", layout="centered")
st.title("Basic Calculator")

st.markdown("---")

# Input fields
num1 = st.number_input("Enter first number:")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
num2 = st.number_input("Enter second number:")

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero.")
            result = None

    if result is not None:
        st.success(f"Result: {result}")
