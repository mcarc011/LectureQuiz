import streamlit as st

def main():
    st.title("Quiz App")
    st.write("Test your knowledge with this fun quiz!")

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

    # Display questions
    for idx, q in enumerate(questions):
        st.subheader(f"Question {idx + 1}")
        user_answer = st.radio(q["question"], q["options"], key=idx)

        # Check answer
        if user_answer == q["answer"]:
            # st.success("Correct!")
            score += 1
        else:
            # st.error(f"Wrong! The correct answer is {q['answer']}.")

    # Final score
    st.write("---")
    st.header(f"Your final score: {score}/{len(questions)}")

    # Feedback based on score
    if score == len(questions):
        st.balloons()
        st.success("Excellent! You're a quiz master!")
    elif score >= len(questions) // 2:
        st.info("Good job! Keep practicing to improve.")
    else:
        st.warning("Don't worry, try again and you'll do better next time!")

if __name__ == "__main__":
    main()
