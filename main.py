import streamlit as st
import uuid
import numpy as np
import pandas as pd
import os

# Function to generate random vectors
def generate_vectors():
    v1 = np.random.randint(-10, 10, size=2)
    v2 = np.random.randint(-10, 10, size=2)
    v3 = np.random.randint(-10, 10, size=2)
    return v1, v2, v3

# Function to check the answer
def check_answer(user_answer, correct_answer):
    return np.array_equal(user_answer, correct_answer)

def magnitude_and_angle(vector):
    magnitude = np.linalg.norm(vector)
    angle =  np.degrees(np.arctan2(vector[1], vector[0])) 
    # Ensure the angle is in the range 0 to 360 degrees
    if angle < 0:
        angle += 360
    mag,angle = round(float(magnitude),2), round(float(angle),2)
    return 'You walked '+str(mag)+' miles at an angle of ' + str(angle) + ' degrees'

# Streamlit app
st.title("Vector Addition")
st.write("You can use this to get the exact answer")
st.markdown("[simulation](https://phet.colorado.edu/sims/html/vector-addition/latest/vector-addition_all.html)")


# # Generate vectors
# if 'v1' not in st.session_state or 'v2' not in st.session_state or 'v3' not in st.session_state:
#     v1, v2, v3 = generate_vectors()
#     v1 = np.array([1,0])
#     v2 = np.array([1,1])
#     v3 = np.array([-1,0])
#     st.session_state.v1, st.session_state.v2, st.session_state.v3 = v1, v2, v3
# else:
#     v1, v2, v3 = st.session_state.v1, st.session_state.v2, st.session_state.v3
v1 = np.array([1,0])
v2 = np.array([0,1])
v3 = np.array([-1,0])

# Display vectors
st.write(f"**1st segment of walk:** {magnitude_and_angle(v1)}")
st.write(f"**2nd segment of walk:** {magnitude_and_angle(v2)}")
st.write(f"**3rd segment of walk:** {magnitude_and_angle(v3)}")

# Input for user answer
st.write(f"**Submit your answer by rounding to nearest integer**")
x_component = st.number_input("Enter your x-coordinate (or how much you went East/West)", step=1)
y_component = st.number_input("Enter your y-coordinate (or how much you went North/South)", step=1)

# Submit button
if st.button("Submit Answer"):
    user_answer = np.array([x_component, y_component])
    correct_answer = v1 + v2 + v3
    
    if check_answer(user_answer, correct_answer):
        st.success("Correct! Well done.")
    else:
        st.error(f"Incorrect. The correct answer is {correct_answer}.")
    
    # Reset for next question
    del st.session_state.v1
    del st.session_state.v2
    del st.session_state.v3

