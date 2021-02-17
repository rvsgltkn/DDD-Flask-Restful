from flask import Flask
from flask_restplus import Api
from config import Config
from application.student.resources.student_resource import api as student_api
from infrastructure.db import DbManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = DbManager.start_db(app)
migrate = Migrate(app, db)


api = Api(app, title='Flask Student Demo',
          version='1.0',
          description='Student Restful Services')

api.add_namespace(student_api, path='/api/v1')


@app.before_first_request
def create_db():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
