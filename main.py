def increment_score():
    global score
    score += 1

def ask_question(question_dictionary):
    print(f"\n{question_dictionary["question"]}")
    for option in question_dictionary["options"]:
        print(option)
    user_answer = input("Enter your answer here: ").lower()
    if user_answer == question_dictionary["answer"].lower():
        print("Correct 👏\nYou gain 1 point.")
        increment_score()
    else:
        print("Incorrect 😭")

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "question": "Which language is primarily used for data analysis and machine learning?",
        "options": ["C++", "JavaScript", "Python", "HTML"],
        "answer": "Python"
    },
    {
        "question": "What planet is known for its rings?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Saturn"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Control Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "What is the result of 3 ** 2 in Python?",
        "options": ["6", "9", "8", "5"],
        "answer": "9"
    },
    {
        "question": "Who wrote the novel '1984'?",
        "options": ["George Orwell", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
        "answer": "George Orwell"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is the file extension for a Python file?",
        "options": [".pt", ".py", ".p", ".python"],
        "answer": ".py"
    }
]

score = 0
