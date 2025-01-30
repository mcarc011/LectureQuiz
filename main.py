import streamlit as st
import uuid
import numpy as np
import pandas as pd
import os

# Generate a unique ID for the session if it doesn't already exist
if 'unique_id' not in st.session_state:
    # Generate a unique ID based on UUID
    st.session_state.unique_id = str(uuid.uuid4())

Simulation = "https://phet.colorado.edu/sims/html/trig-tour/latest/trig-tour_all.html"

def load_scores():
    if os.path.exists('scores.csv'):
        return pd.read_csv('scores.csv')
    else:
        return pd.DataFrame(columns=["id", "score"])

def main():
    st.title("Trigonometry")
    st.write("Please refrain from using google, a calculator, or AI. Instead use this!" )
    st.write("Unit Circle Simulation : [Simulation](%s)" %Simulation)

    # Questions and answers
    questions = [
        {
            "question": "What angle in radians is associated with the northwest direction?",
            "options": ["$\\frac{\\pi}{4}$", "$\\frac{3\\pi}{4}$", "$\\frac{5\\pi}{4}$", "$\\frac{7\\pi}{4}$"],
            "answer":  "$\\frac{3\\pi}{4}$",
        },
        {
            "question": "At what angle do I walk if I walk 0.5mi east and 0.866mi north?",
            "options": ["30\u00b0", "45\u00b0", "60\u00b0", "90\u00b0"],
            "answer": "60\u00b0",
        },
        {
            "question": "Which of these will tell me how far east I went if I walked 30\u00b0 southeast for 20 miles?",
            "options": [
                "20 cos(30\u00b0)",
                "30\u00b0 cos(20)",
                "20 sin(30\u00b0)",
                "30\u00b0 sin(20)"
            ],
            "answer": "20 cos(30\u00b0)",
        },
        {
            "question": "Which of these will tell me how far south I went if I walked 30\u00b0 southeast for 20 miles?",
            "options": [
                "20 cos(30\u00b0)",
                "30\u00b0 cos(20)",
                "20 sin(30\u00b0)",
                "30\u00b0 sin(20)"
            ],
            "answer": "20 sin(30\u00b0)",
        },
                {
            "question": "At what angle is sin $\\theta$ and cos $\\theta$ negative?",
            "options": ["$\\frac{\\pi}{4}$", "$\\frac{3\\pi}{4}$", "$\\frac{5\\pi}{4}$", "$\\frac{7\\pi}{4}$"],
            "answer":  "$\\frac{5\\pi}{4}$",
        },
    ]

    score = 0

    tab1, tab2 = st.tabs(["Quiz", "Scores"])

    with tab1:
        # Display questions
        answers_submitted = False
        user_answer = {}
        for idx, q in enumerate(questions):
            st.subheader(f"Question {idx + 1}")
            user_answer[idx] = st.radio(q["question"], q["options"], key=idx)

        
        if st.button("Submit Quiz"):
            answers_submitted = True

        if answers_submitted:
            for idx, q in enumerate(questions):
                if user_answer[idx] == q["answer"]:
                    st.success(f"Question {idx + 1}: Correct!")
                    score += 1
                else:
                    st.error(f"Question {idx + 1}: Wrong!.")

            scores_data = load_scores()
            user_score = pd.DataFrame([{"id": st.session_state.unique_id, "score": score/len(questions)}])
            scores_data = pd.concat([scores_data, user_score], ignore_index=True)
            scores_data.to_csv('scores.csv', index=False)
            
            answers_submitted = False

        if score > 0:
            st.write("---")
            st.header(f"Your final score: {score}/{len(questions)}")


    with tab2:
        st.header("Average Scores")
        try:
            csv_data = pd.read_csv('scores.csv')
            unique_ids = csv_data.iloc[:, 0].unique()
            highscores = []
            st.write(len(unique_ids))
            for uid in unique_ids:
                highscores += [csv_data[csv_data.iloc[:, 0] == uid].iloc[:, 1].max()]
            avg_score = np.mean(highscores)
        except:
            avg_score = 0

        st.write(round(100*avg_score,2))

        if st.button("Reset"):
            empty = pd.DataFrame(columns=["id", "score"])
            empty.to_csv('scores.csv',index=False)

if __name__ == "__main__":
    main()
