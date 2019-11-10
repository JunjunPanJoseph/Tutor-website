from app.database.dbClass import *
from app import dbConfig


class DataManager:
    def __init__(self, db):
        self.db = db

    def get_course(self, course_id):
        return_list = []
        session = self.db.getSession()
        for instance in session.query(CourseList).filter(CourseList.id == course_id):
            return_list.append(instance)
        session.close()
        if not return_list:
            return None
        return return_list[0]

    def getCourseList(self):
        return_list = []
        session = self.db.getSession()
        for instance in session.query(CourseList).order_by(CourseList.name):
            return_list.append(instance)
        session.close()
        return return_list

    @staticmethod
    def get_subscribed_course_list():
        return []

    def get_recent_article_list(self, n=20):
        return_list = []
        session = self.db.getSession()
        for instance in session.query(Artical).filter_by(state=1).order_by(Artical.timelastedit.desc())[0:n]:
            return_list.append(instance)
        session.close()
        return return_list

    def get_course_class(self, course_id):
        return_list = []
        session = self.db.getSession()
        for instance in session.query(CourseContent, Artical).filter_by(courseid=course_id).filter(
                CourseContent.artical == Artical.id):
            return_list.append(instance)
        session.close()
        return return_list

    def get_article(self, article_id):
        return_list = []
        session = self.db.getSession()
        for instance in session.query(Artical).filter(Artical.id == article_id):
            return_list.append(instance)
        session.close()
        if not return_list:
            return None
        return return_list[0]

    def get_questions(self, article_id):
        # TODO: Connect it to the database
        return_list = []
        return return_list

    def setArticle(self):
        pass


dataManager = DataManager(dbConfig)
