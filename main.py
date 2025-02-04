import streamlit as st
import numpy as np

# Function to generate random vectors
def generate_vectors():
    v1 = np.random.randint(-10, 10, size=2)
    v2 = np.random.randint(-10, 10, size=2)
    return v1, v2

# Function to check the answer
def check_answer(user_answer, correct_answer):
    return np.array_equal(user_answer, correct_answer)

# Streamlit app
st.title("Vector Addition Quiz")

# Generate vectors
if 'v1' not in st.session_state or 'v2' not in st.session_state:
    v1, v2 = generate_vectors()
    st.session_state.v1, st.session_state.v2 = v1, v2
else:
    v1, v2 = st.session_state.v1, st.session_state.v2

# Display vectors
st.write(f"**Vector A:** {v1}")
st.write(f"**Vector B:** {v2}")

# Input for user answer
x_component = st.number_input("Enter the x-component of A + B:", step=1)
y_component = st.number_input("Enter the y-component of A + B:", step=1)

# Submit button
if st.button("Submit Answer"):
    user_answer = np.array([x_component, y_component])
    correct_answer = v1 + v2
    
    if check_answer(user_answer, correct_answer):
        st.success("Correct! Well done.")
    else:
        st.error(f"Incorrect. The correct answer is {correct_answer}.")
    
    # Reset for next question
    del st.session_state.v1
    del st.session_state.v2

# Instructions
st.sidebar.header("Instructions")
st.sidebar.write("1. Add the corresponding components of vectors A and B.")
st.sidebar.write("2. Enter the x and y components of the resulting vector.")
st.sidebar.write("3. Click 'Submit Answer' to check your response.")
