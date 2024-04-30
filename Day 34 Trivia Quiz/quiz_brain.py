import html


class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.questions_list = qlist
        self.score = 0

    def next_question(self, ans):
        question = html.unescape(self.questions_list[self.question_number].text)
        if ans is not None:
            if self.check_score(ans):
                self.score += 1
        self.question_number += 1
        return question

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_score(self, ans: bool) -> bool:
        if ans == self.questions_list[self.question_number].answer:
            return True
        else:
            return False
