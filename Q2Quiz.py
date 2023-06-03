def main():
    score = 0

    with open('questions.txt', 'r') as file:
        lines = file.readlines()
        num_questions = len(lines) // 6

        for i in range(num_questions):
            question = lines[i * 6].strip()
            answers = lines[i * 6 + 1:i * 6 + 5]
            correct_answer = lines[i * 6 + 5].strip()

            print(f"\nQuestion {i+1}: {question}")
            for j, answer in enumerate(answers):
                print(f"{chr(ord('A') + j)}. {answer.strip()}")

            user_answer = input("Enter your answer (A, B, C, or D): ")
            if user_answer.upper() == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")

    print(f"\nQuiz completed. Your score is {score}/{num_questions}.")


if __name__ == '__main__':
    main()
