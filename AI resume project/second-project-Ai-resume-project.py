from sqlalchemy import column, Integer, String,Text,ForeignKey
from db import base
class User(base):
    __tablename__ = "users"
    id = column(Integer, primary_key=True)
    email = column(String(100), unique=True)
    password = column(String(100))



    class Report (Base):
        __tablename__ = "reports"
        id = column(Integer, primary_key=True)
    user_id = column(Integer, ForeignKey("users.id"))
    resume_text = column(Text)
    result = column(Text)
    


 