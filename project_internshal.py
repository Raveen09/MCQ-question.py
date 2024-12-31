import random
import time
''' code is for making student choice that a person can choose mcq ques from option set and work according to it '''
class MockTest:
    def __init__(self, paper1_questions, paper2_questions):
        self.paper1_questions = paper1_questions
        self.paper2_questions = paper2_questions
        self.user_answers = []
        self.start_time = None
        self.end_time = None

    def start_test(self, paper_number, time_limit):
        try:
            if paper_number not in [1, 2]:
                raise ValueError("Invalid paper number. Please choose 1 or 2.")
            
            questions = self.paper1_questions if paper_number == 1 else self.paper2_questions
            self.user_answers = [None] * len(questions)
            self.start_time = time.time()
            print(f"Starting Paper {paper_number}... You have {time_limit} seconds.")
            
            for i, question in enumerate(questions):
                print(f"Q{i + 1}: {question}")
                answer = input("Your answer: ")
                self.user_answers[i] = answer
                
                if time.time() - self.start_time > time_limit:
                    print("Time's up!")
                    break

            self.end_time = time.time()
            print("Test completed.")
            self.provide_feedback()

        except Exception as e:
            print(f"An error occurred: {e}")

    def provide_feedback(self):
        total_time = self.end_time - self.start_time
        print(f"Total time taken: {total_time:.2f} seconds.")
        # Here you can add AI-driven feedback logic
        print("Feedback: Analyze your performance based on your answers.")

# Samplquestions for Paper 1 and Paper 2
paper1_questions = [
    "What is the capital of France?",
    "Who wrote 'Hamlet'?",
    "What is the boiling point of water?",
    # Add more questions as needed
]

paper2_questions = [
    "What is the largest planet in our solar system?",
    "Who painted the Mona Lisa?",
    "What is the chemical symbol for gold?",
    # Add more questions as needed
]

if __name__ == "__main__":
    mock_test = MockTest(paper1_questions, paper2_questions)
    try:
       paper_choice = int(input("Choose paper (1 or 2): "))
        time_limit = int(input("Set time limit in seconds: "))
        mock_test.start_test(paper_choice, time_limit)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
