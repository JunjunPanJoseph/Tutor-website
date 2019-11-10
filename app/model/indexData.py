from app.model import baseData
from app.model import articalData

class RecommandData:
	def __init__(self):
		self.introduction = ""
		self.pictures = []
	def setIntroduction(self, introduction):
		self.introduction = introduction
	def addPicture(self, picture):
		self.pictures.append(picture)
	def getIntroduction(self):
		return self.introduction
	def getPictures(self):
		return pictures
	def getPicturesSize(self):
		return len(self.pictures)
	def loadData(self):
		for i in range(5):
			self.pictures.append(PictureStruct("Pic" + (i + 1), 'image/index/recommended/' + (i + 1) +'.jpg'))


class IndexData(baseData.BaseData):
	def __init__(self, left_title):
		super(IndexData, self).__init__(left_title)
		self.recommandData = RecommandData()
		self.subscriptedArticalList = []
		self.recentArticalList = []
	def bootstrap(self, username = None):
		self.recommandData.load()
		#Load recentArtical...
		#Load user subscripted artical...
		if (username != None):
			pass
		return self
	def setSubscriptedArticalList(self, subscriptedArticalList):
		self.subscriptedArticalList = subscriptedArticalList
	def getSubscriptedArticalList(self):
		return self.subscriptedArticalList
	def setRecentArticalList(self, recentArticalList):
		self.recentArticalList = recentArticalList
	def getRecentArticalList(self):
		return self.recentArticalList
	