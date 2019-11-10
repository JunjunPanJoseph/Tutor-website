from flask import Flask
from flask_bootstrap import Bootstrap
from app.database import dbClass


app = Flask(__name__)
bootstrap = Bootstrap(app)
dbConfig = dbClass.DatabaseConfig()

from app import routes
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)