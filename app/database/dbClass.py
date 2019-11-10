from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.types import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

String64 = String(64)

class DatabaseConfig():
    server = "postgresql"
    username = 'ring_admin'
    password = 'lin0729*****'
    address = "localhost"
    port = 5432
    database = "websiteDB"
    engine = None
    Session = None
    def makeCommand(self):
        command = "{0}://{1}:{2}@{3}:{4}/{5}"\
            .format(self.server, self.username, self.password,
            self.address, self.port, self.database)
        return command
    def getEngine(self):
        if (self.engine == None):
            self.engine = create_engine(self.makeCommand())
        return self.engine
    def getSession(self):
        if (self.engine == None):
            self.getEngine()
        if (self.Session == None):
            self.Session = sessionmaker(bind=self.engine)
        return self.Session()
        

#Generate SQLORM base class.
Base = declarative_base()
class User(Base):
    #Table name
    __tablename__ = 'users'
    email = Column(String64, primary_key=True)
    name = Column(String64, nullable=False)
    password = Column(String64, nullable=False)
    authority = Column(CHAR(), nullable=False)
    qq = Column (String64)
    wechat = Column (String64)
    
class Artical(Base):
    __tablename__ = 'articals'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    author = Column(String64, ForeignKey('users.email'), nullable=False)
    title = Column(String(128), nullable=False)
    abstract = Column(String(256), nullable=False)
    state = Column(Integer(), nullable=False)
    htmlcontent = Column(VARCHAR, nullable=False)
    timepublish = Column(TIMESTAMP, nullable=False)
    timelastedit = Column(TIMESTAMP, nullable=False)
    keywords = Column(String64, nullable=False)
    
class Commit(Base):
    __tablename__ = 'commits'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    artical = Column(Integer(), ForeignKey('articals.id'), nullable=False)
    author = Column(String64, ForeignKey('users.email'), nullable=False)
    state = Column(Integer(), nullable=False)
    htmlcontent = Column(VARCHAR, nullable=False)

class CourseList(Base):
    __tablename__ = 'courses'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    name = Column(String64, nullable=False)
    title = Column(String(128), nullable=False)
    #artical fore-key
    description = Column(VARCHAR, nullable=False)
    advice = Column(VARCHAR)
    htmlcontent = Column(VARCHAR, nullable=False)
class CourseContent(Base):
    __tablename__ = 'coursecontent'
    courseid = Column(Integer(), ForeignKey('courses.id'), primary_key=True)
    label  = Column(String64, primary_key=True)
    artical = Column(Integer(), ForeignKey('articals.id'), primary_key=True)
#create all tables
def createAllTable():
    #Config
    databaseConfig = DatabaseConfig()
    #bind engine
    engine = databaseConfig.getEngine()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    createAllTable()