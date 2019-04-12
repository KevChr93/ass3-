from sqlalchemy import Integer, Column, String, Float
from sqlalchemy.sql import func
from animeHub import db

 

#db.create_all()
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    role = Column(Integer, nullable=False)

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def toDict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }


class Anime(db.Model):
    __tablename__ = 'Anime_List'
    Anime_Id = Column(Integer, primary_key=True, nullable=False)
    Name = Column(String(100), unique=True, nullable=False)
    Genre = Column(String(200), nullable=False)
    Type = Column(String(20), nullable=False)
    Episodes = Column(Integer, nullable=False)
    Rating = Column(Float, nullable=False)
    Members = Column(Integer)

    def __init__(self, id, name, gen, Atype, epi, rating, mem):
        self.Anime_Id = id
        self.Name = name
        self.Genre = gen
        self.Type = Atype
        self.Episodes = epi
        self.Rating = rating
        self.Members = mem

    def toDict(self):
        return {
            'Anime_Id': self.Anime_Id,
            'Name': self.Name,
            'Genre': self.Genre,
            'Type': self.Type,
            'Episodes': self.Episodes,
            'Rating': self.Rating,
            'Members': self.Members
        }
