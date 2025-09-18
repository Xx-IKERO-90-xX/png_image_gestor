from extensions import db

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(300), unique=True)
    passwd = db.Column(db.String(300), unique=True)
    mc_console = db.Column(db.Boolean)
    pig = db.Column(db.Boolean)

    def __init__(self, username, passwd, mc_console=False, pig=False):
        self.username = username
        self.passwd = passwd
        self.mc_console = mc_console
        self.pig = pig