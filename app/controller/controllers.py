from flask import Flask, render_template, session, redirect, url_for, flash
from app import app
from app.model import models


def test():
    return render_template('TestPages/helloWorld.html', testData=models.test_model())


def index():
    return render_template('index.html', data=models.load_index_page_data())


def courseTutorial(course_id):
    return render_template('tutorial.html', data=models.load_tutorial_course_page_data(int(course_id)))


def getArticle(article_id):
    return models.load_quiz_data(article_id).serialize()
    # return models.load_article_data(article_id).serialize()


def getQuiz(article_id):
    return render_template('quiz.html', data=models.load_quiz_data(int(article_id)))
