from flask import render_template
from flask.json import jsonify

from app.model import articalData


class Question:
    def __init__(self, qid, description, question):
        self.qid = qid
        self.description = description
        self.question = question


class QuestionMultipleChoice(Question):
    def __init__(self, qid, description, question):
        super(QuestionMultipleChoice, self).__init__(qid, description, question)
        self.choices = []

    def add_choice(self, cid, text, commit, answer):
        self.choices.append({'cid': cid, 'text': text, 'commit': commit, 'answer': answer})

    def get_choices(self):
        return self.choices


class QuestionTextfield(Question):
    def __init__(self, qid, description, question):
        super(QuestionTextfield, self).__init__(qid, description, question)
        self.fields = []

    def add_textfield(self, tid, text, default_text, commit, answer, size):
        self.fields.append({'tid': tid, 'text': text, 'defaultText': default_text,
                            'commit': commit, 'answer': answer, 'size': size})

    def get_fields(self):
        return self.fields


class QuizArticleData(articalData.ArticalData):
    def __init__(self, dbobj):
        super(QuizArticleData, self).__init__(dbobj)
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_questions(self):
        return self.questions

    def serialize(self):
        retval = self.to_dir()
        retval['htmlcontent'] += render_template('quiz.html', data=self)
        return jsonify(retval)

