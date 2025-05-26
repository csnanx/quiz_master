import random

def ask_question(question_dictionary):
    print(f"\n{question_dictionary["question"]}")
    for option in question_dictionary["options"]:
        print(option)
    user_answer = input("Enter your answer here: ")
    return user_answer.lower() == question_dictionary["answer"].lower()

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    for question_dict in questions:
        correct = ask_question(question_dict)
        if correct:
            print("Congrats! 👏\nYou gain 1 point.")
            score += 1
        else:
            print("Incorrect 😭")
    return score

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for data analysis and machine learning?",
        "options": ["A. C++", "B. JavaScript", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What planet is known for its rings?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Processing Unit", "D. Control Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. lambda"],
        "answer": "B"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "question": "What is the result of 3 ** 2 in Python?",
        "options": ["A. 6", "B. 9", "C. 8", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Who wrote the novel '1984'?",
        "options": ["A. George Orwell", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "What is the file extension for a Python file?",
        "options": ["A. .pt", "B. .py", "C. .p", "D. .python"],
        "answer": "B"
    }
]

score = run_quiz(questions)
print(f"\nYour score is: {score}")

if score > 8:
    print("Excellent!")
elif score > 5:
    print("Good job!")
else:
    print("Keep practicing!")
