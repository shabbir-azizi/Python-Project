from flask import Flask, render_template, request, redirect, session
from db import base, engine, sessionlocal
import models
import PyPDF2
import docx
import json

app = Flask(__name__)


app.secret_key="secret123"

base.metadata.create_all(bind=engine)


@app.route("/")                                                

def home():
    if "user" in session :
        return redirect ("/dashboard")
    
    return redirect("/login")


#----SIGNUP
frist-project-Ai-resum.route("/signup", methods=["GET", "POST"])
def signup():
        db = sessionlocal()

        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            existing_user = db.query(models.User).filter_by(email=email).first()
            if existing_user:
                return "User already exists"
            user = models.User (email=email, password=password)
            db.add(user)
        
        
        if __name__ == '__main__':
             app.run(debug=True)
                                