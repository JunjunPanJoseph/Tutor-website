from flask import jsonify


class ArticalData():
    def __init__(self, dbObj=None):
        if (dbObj != None):
            self.id = dbObj.id
            self.author = dbObj.author
            self.title = dbObj.title
            self.abstract = dbObj.abstract
            self.state = dbObj.state
            self.htmlcontent = dbObj.htmlcontent
            self.timepublish = dbObj.timepublish
            self.timelastedit = dbObj.timelastedit
            self.keywords = dbObj.keywords.split('|')

    def to_dir(self):
        retval = {}
        retval['id'] = self.id
        retval['author'] = self.author
        retval['title'] = self.title
        retval['abstract'] = self.abstract
        retval['state'] = self.state
        retval['htmlcontent'] = self.htmlcontent
        retval['timepublish'] = self.timepublish
        retval['timelastedit'] = self.timelastedit
        retval['keywords'] = self.keywords
        return retval

    def serialize(self):
        retval = self.to_dir()
        return jsonify(retval)
