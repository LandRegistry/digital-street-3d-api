import os

from flask_script import Manager
from digital_street_3d_api.main import app
from flask_migrate import Migrate, MigrateCommand
from digital_street_3d_api.models import *    # noqa
from digital_street_3d_api.extensions import db

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def runserver(port=9998):
    """Run the app using flask server"""

    os.environ["PYTHONUNBUFFERED"] = "yes"
    os.environ["LOG_LEVEL"] = "DEBUG"
    os.environ["COMMIT"] = "LOCAL"

    app.run(debug=True, port=int(port))


if __name__ == "__main__":
    manager.run()
