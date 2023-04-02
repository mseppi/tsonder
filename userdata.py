from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def register(name, password):
    hash_value=generate_password_hash(password)
    sql="INSERT INTO users (name, password) VALUES (:username, :password)"
    db.session.execute(sql, {"name":name})