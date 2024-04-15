from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer'],))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

print(f"You've completed the quiz! \nYour final score is {new_quiz.score} out of {new_quiz.question_number+1}")
