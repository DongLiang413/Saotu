# -*- encoding=UTF-8 -*-
from saotu import app, db
from flask_script import Manager
from saotu.models import User
import random

manager = Manager(app)


@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    for i in range(0, 10):
        db.session.add(User('User' + str(i), 'c' + str(i)))
    db.session.commit()


if __name__ == '__main__':
    # init_database()
    manager.run()
