class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}/ {current_question.text} True/False: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("That is right!")
            self.score += 1
        else:
            print("That is wrong...")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number} \n")

    def print_score(self):
        print(
            f"You've completed the Quizz!\nYour final score is {self.score}/{self.question_number}")
