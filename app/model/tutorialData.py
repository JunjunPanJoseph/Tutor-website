from app.model import baseData
from app.model import articalData

class TutorialData(baseData.BaseData):
    def __init__(self, left_title):
        super(TutorialData, self).__init__(left_title)
        self.artical = None
    def setArtical(self, artical):
        self.artical = artical
    def getArtical(self):
        return self.artical