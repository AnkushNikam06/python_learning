questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Colombo", "C. Delhi", "D. Rome"],
        "correct_answer": "Delhi",
        "prize": 1000
    },
    {
        "question": "Who found the country India?",
        "options": ["A. Shakespeare", "B. Sikandar", "C. Newton", "D. Columbus"],
        "correct_answer": "Columbus",
        "prize": 10000
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "correct_answer": "Jupiter",
        "prize": 100000
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Oxygen", "B. Osmium", "C. Ozone", "D. Opium"],
        "correct_answer": "Oxygen",
        "prize": 1000000
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Diamond", "C. Iron", "D. Platinum"],
        "correct_answer": "Diamond",
        "prize": 10000000
    }
]

print("***Welcome to Kaun Banega CrorePati***")

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    answer = input("Please enter your answer: ").strip()
    if answer == question_data["correct_answer"]:
        print(f"Correct Answer! You won INR {question_data['prize']}")
        return question_data["prize"]
    else:
        print("Wrong Answer! Game Over.")
        return 0

def main():
    total_prize = 0

    for i, question_data in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        prize = ask_question(question_data)
        
        if prize == 0:
            print(f"Total prize amount: INR {total_prize}")
            break
        
        total_prize += prize
        
    else:
        print(f"Congratulations! You took home INR {total_prize}")

if __name__ == "__main__":
    main()
