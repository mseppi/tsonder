from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from flask import session
from os import urandom


def register(name, password, role):
    try:   
        hash_value=generate_password_hash(password)
        sql="INSERT INTO users (name, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    except:
        db.session.rollback()
        return False
    return login(name, password)

def login(name, password):
    sql = "SELECT password, id, role FROM users WHERE name=:name"
    outcome = db.session.execute(sql, {"name":name})
    user = outcome.fetchone()
    if check_password_hash(user[0], password):
        if not user:
            return False
        session["user_name"]=name
        session["user_id"]=user[1]
        session["user_role"]=user[2]
        session["csrf_token"]=urandom(16).hex()
        return True
    return False
