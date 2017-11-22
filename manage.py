from flask_script import Manager
from blockchain import app

manager = Manager(app)


# reset the database and create two artists
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    coldplay = Artist(name='Coldplay', about='Coldplay is a British rock band.')
    maroon5 = Artist(name='Maroon 5', about='Maroon 5 is an American pop rock band.')
    db.session.add(coldplay)
    db.session.add(maroon5)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
