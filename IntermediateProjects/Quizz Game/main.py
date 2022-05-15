from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain
from quiz_brain import QuizzBrain

question_bank = []


for question_dic in question_data:
    text = question_dic["question"]
    answer = question_dic["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

quizz.print_score()
