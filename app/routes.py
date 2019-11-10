from flask import Flask, render_template, session, redirect, url_for, flash
from flask import jsonify
from app import app
from app.controller import controllers


@app.route('/test')
def test():
    return controllers.test()


@app.route('/')
def mainPage():
    return controllers.index()


@app.route('/index')
def index():
    return controllers.index()


@app.route('/tutorial/<courseid>')
def courseTutorial(courseid):
    return controllers.courseTutorial(courseid)


@app.route('/artical/<article_id>')
def get_article(article_id):
    return controllers.getArticle(article_id)


@app.route('/quiz/<article_id>')
def get_quiz(article_id):
    return controllers.getQuiz(article_id)
