from flask_sqlalchemy import SQLAlchemy
from animeHub.models import User, Anime

def createUser(new_user):
    try:
        u = User(new_user['username'], new_user['email'], new_user['password'],new_user['role'])#create person object using contructor
        db.session.add(u)
        db.session.commit()# save object
    except error:
        return {"message":"Error "+error, "code":500}
    finally:
        return {"message":u.toDict(), "code":201}
        
def updatePerson(new_user, id):
    try:
        u = User.query.get(id)
        u.name = new_user['name'] 
        u.email = new_user['email'] 
        u.password = new_user['password'] 
        u.role = new_user['role'] 
        db.session.commit()#save object
    except error:
        return {"message":"Error "+error, "code":500}
    finally:
        return {"message": u.toDict(), "code":202}

def deleteAnime(id):
    try:
        u = Anime.query.get(id)
        db.session.delete(u)#delete object from database
        db.session.commit()#save changes
    except error:
        return {"message":"Database error"+error, "code":500}
    finally:
        return {"message": "Record Deleted", "code": 204}

