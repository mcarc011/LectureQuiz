import streamlit as st
import uuid
import numpy as np

def main():
    st.title("Quiz App")
    st.write("Test your knowledge with this fun quiz!")

    quiz_id = st.session_state.get("quiz_id", str(uuid.uuid4()))
    # Questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars",
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": [
                "Harper Lee",
                "Mark Twain",
                "Ernest Hemingway",
                "F. Scott Fitzgerald",
            ],
            "answer": "Harper Lee",
        },
    ]

    score = 0

    tab1, tab2 = st.tabs(["Quiz", "Scores"])

    with tab1:
        # Display questions
        for idx, q in enumerate(questions):
            st.subheader(f"Question {idx + 1}")
            user_answer = st.radio(q["question"], q["options"], key=idx)

            # Check answer
            if user_answer == q["answer"]:
                # st.success("Correct!")
                score += 1
            else:
                pass
                # st.error(f"Wrong! The correct answer is {q['answer']}.")

        # Final score
        st.write("---")

        with open('scores.txt','w') as f:
            ftext = f.readlines()
            if quiz_id in ','.join(ftext):
                ftext = [fi for fi in ftext if quiz_id not in fi]
            ftext += [quiz_id + ':'+ {score}/{len(questions)}]
            f.write('\n'.join(ftext))
            f.close()

        # Feedback based on score
        if score == len(questions):
            st.balloons()
            st.success("Excellent! You're a quiz master!")
        elif score >= len(questions) // 2:
            st.info("Good job! Keep practicing to improve.")
        else:
            st.warning("Don't worry, try again and you'll do better next time!")

    with tab2:
        st.header("Average Scores")
        avg_score = 0 
        with open('scores.txt','w') as f:
            ftext = f.readlines()
            avg_score = np.average([float(fi.split(':')[1]) for fi in ftext])

        st.write(avg_score)

if __name__ == "__main__":
    main()
