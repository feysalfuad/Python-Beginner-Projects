import random

print("🎮 Welcome to Python Quiz!")

play_again = "yes"

def run_quiz():
    score = 0

    questions = [
        {
            "question": "What does print() do?",
            "options": ["Store data", "Takes input", "Shows output"],
            "answer": "Shows output"
        },
        {
            "question": "What does a variable do?",
            "options": ["Converts text", "Stores data", "Takes input"],
            "answer": "Stores data"
        },
        {
            "question": "What does int do?",
            "options": ["Converts text to number", "Takes input", "Repeats code"],
            "answer": "Converts text to number"
        },
        {
            "question": "What does input() do?",
            "options": [
                "Takes information from the user",
                "Checks a condition",
                "Repeats code"
            ],
            "answer": "Takes information from the user"
        },
        {
            "question": "What does if do?",
            "options": [
                "Checks a condition",
                "Runs code forever",
                "Creates a function"
            ],
            "answer": "Checks a condition"
        },
        {
            "question": "What does else do?",
            "options": [
                "Runs if condition is false",
                "Repeats code multiple times",
                "Creates a function"
            ],
            "answer": "Runs if condition is false"
        },
        {
            "question": "What is a loop?",
            "options": [
                "Repeats code multiple times",
                "Stores data",
                "Checks a condition"
            ],
            "answer": "Repeats code multiple times"
        },
        {
            "question": "What does range() do?",
            "options": [
                "Controls loop repetitions",
                "Creates a function",
                "Stores text data"
            ],
            "answer": "Controls loop repetitions"
        },
        {
            "question": "What is a function?",
            "options": [
                "Reusable block of code",
                "Checks a condition",
                "Repeats code forever"
            ],
            "answer": "Reusable block of code"
        },
        {
            "question": "What is indentation?",
            "options": [
                "Spaces that define code structure",
                "Repeats code",
                "Stores data"
            ],
            "answer": "Spaces that define code structure"
        }
    ]

    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])

        options = q["options"]
        random.shuffle(options)

        labels = ["A", "B", "C"]

        correct_index = options.index(q["answer"])

        for i in range(len(options)):
            print(labels[i] + ".", options[i])

        answer = input("Enter A, B or C: ").upper()

        if answer == labels[correct_index]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print("\nFinal Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if score == len(questions):
        print("🏆 Perfect!")
    elif score >= len(questions)//2:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")

while True:
    run_quiz()
    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("👋 Thanks for playing!")
        break
