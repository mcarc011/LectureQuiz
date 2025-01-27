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
    st.write("Unit Circle Simulation : [Simulation](%s)")

    # Questions and answers
    questions = [
        {
            "question": "What is cos($\\pi$)?",
            "options": ["-1", "0", "1"],
            "answer": "-1",
        },
        {
            "question": "What angle is associated with $\\frac{\\pi}{2}$?",
            "options": ["30\u00b0", "45\u00b0", "90\u00b0", "180\u00b0"],
            "answer": "45\u00b0",
        },
        {
            "question": "What is sin($6\\pi$)?",
            "options": [
                "-1",
                "0",
                "1",
            ],
            "answer": "0",
        },
                {
            "question": "What is sin$^{2}\\theta$ + cos$^{2}\\theta$?",
            "options": [
                "-1",
                "0",
                "1",
            ],
            "answer": "1",
        },
                {
            "question": "At what angle is sin $\\theta$ = -cos $\\theta$",
            "options": [
                "$\\frac{\\pi}{4}$",
                "$\\frac{\\pi}{2}$",
                "$\\frac{3\\pi}{4}$",
                "$\\pi$",
            ],
            "answer": "$\\frac{3\\pi}{4}$",
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
