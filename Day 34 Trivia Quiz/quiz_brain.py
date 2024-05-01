import html


class QuizBrain:
    def __init__(self, qlist):
        self.question_number = -1
        self.questions_list = qlist

    def next_question(self):
        self.question_number += 1
        question = html.unescape(self.questions_list[self.question_number].text)
        return question

    def still_has_question(self):
        return self.question_number < len(self.questions_list)-1

    def check_score(self, ans) -> bool:
        if ans == self.questions_list[self.question_number].answer:
            return True
        else:
            return False
