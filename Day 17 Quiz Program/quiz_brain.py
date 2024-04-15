class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.questions_list = qlist
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)?:")
        self.check_score(answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right')
            self.score += 1
        else:
            print('You got it wrong')
        print(f'You current score is {self.score}/{self.question_number+1}\n')
