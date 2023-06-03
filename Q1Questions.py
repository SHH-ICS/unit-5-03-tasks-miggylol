def main():
    with open('questions.txt', 'w') as file:
        for _ in range(3):  # Assuming you want to store 3 questions
            question = input("Enter the question: ")
            answer1 = input("Enter the first answer: ")
            answer2 = input("Enter the second answer: ")
            answer3 = input("Enter the third answer: ")
            answer4 = input("Enter the fourth answer: ")
            correct_answer = input("Enter the letter of the correct answer: ")

            file.write(f"{question}\n")
            file.write(f"{answer1}\n")
            file.write(f"{answer2}\n")
            file.write(f"{answer3}\n")
            file.write(f"{answer4}\n")
            file.write(f"{correct_answer}\n")

    print("Questions stored in questions.txt.")


if __name__ == '__main__':
    main()
