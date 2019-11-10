class PictureStruct:
	def __init__(self, title, url):
		self.title = title
		self.url = url
	def getTitle(self):
		return self.title
	def getURL(self):
		return self.url
	def getPicture(self):
		return None
class Header:
	def __init__(self):
		self.backgroundPic = PictureStruct('backGround', 'image/base/header_background.png')
		self.logo = PictureStruct('logo', 'image/base/logo.png')
	def getBackgroundURL(self):
		return self.backgroundPic.getURL()
	def getLogoURL(self):
		return self.logo.getURL()
class ListComposite:
	def __init__(self, name):
		self.name = name
		self.children = []
		self.url = None
		self.id = 0
	def getName(self):
		return self.name
	def getChildren(self):
		return self.children
	def getURL(self):
		return self.url
	def isLeaf(self):
		return len(self.children) == 0 
	def setURL(self, newUrl):
		self.url = newUrl
	def addChild(self, newChild):
		self.children.append(newChild)
	def setID(self, id):
		self.id = id
	def getID(self):
		return self.id
class LeftRow:
	def __init__(self, title):
		self.title = title
		self.content = []
		self.id = 0
	def getContentSize(self):
		return len(self.content)
	def getTitle(self):
		return self.title
	def getContent(self):
		return self.content
	def addContent(self, newCompoosite):
		self.content.append(newCompoosite)
	def setContent(self, newContent):
		self.content = newContent

generalHeader = Header()
class BaseData:
	def __init__(self, left_title):
		self.header = generalHeader
		self.leftRow = LeftRow(left_title)
	def getHeader(self):
		return self.header
	def getLeftRow(self):
		return self.leftRow