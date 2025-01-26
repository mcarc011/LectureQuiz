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
        answers_submitted = False
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
                    st.error(f"Question {idx + 1}: Wrong! The correct answer is {q['answer']}.")

            with open('scores.csv','r+') as f:
                ftext = f.readlines()
                if quiz_id in ','.join(ftext):
                    ftext = [fi for fi in ftext if quiz_id not in fi]
                ftext += [quiz_id + ','+ str(score/len(questions))]
                f.write('\n'.join(ftext))
                f.close()
                answers_submitted = False


            # Final score
        if score > 0:
            st.write("---")
            st.header(f"Your final score: {score}/{len(questions)}")


    with tab2:
        st.header("Average Scores")
        with open('scores.csv','r') as f:
            ftext = f.readlines()
            try:
                avg_score = np.average([float(fi.split(',')[1]) for fi in ftext])
            except:
                avg_score = 0 
            f.close()

        st.write(avg_score)

if __name__ == "__main__":
    main()
