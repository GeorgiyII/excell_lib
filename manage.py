import os

from flask_script import Manager

from service_app.app import app

manager = Manager(app)


@manager.command
def runserver():
    app.run(
        host='127.0.0.1',
        port=int(os.environ.get('PORT', 8000)),
        debug=bool(os.environ.get('DEBUG', ''))
        )


if __name__ == '__main__':
    manager.run()
