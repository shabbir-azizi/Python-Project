import json

from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.utils import secure_filename

from db import engine, sessionlocal, Base
import models
from ai import analyze_resume

app = Flask(__name__)
app.secret_key = "secret123"

Base.metadata.create_all(bind=engine)


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        db = sessionlocal()
        try:
            existing_user = db.query(models.User).filter_by(email=email).first()
            if existing_user:
                return "User already exists"
            user = models.User(email=email, password=password)
            db.add(user)
            db.commit()
        finally:
            db.close()
        return redirect(url_for("login"))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        db = sessionlocal()
        try:
            user = db.query(models.User).filter_by(email=email, password=password).first()
        finally:
            db.close()

        if user:
            session["user"] = user.email
            return redirect(url_for("dashboard"))
        return "Invalid credentials"

    return render_template("login.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    result = None
    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume", "")

        file = request.files.get("file")
        if file and file.filename != "":
            filename = secure_filename(file.filename)
            if filename.lower().endswith(".pdf"):
                try:
                    import PyPDF2
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF error: {str(e)}"}
            elif filename.lower().endswith(".docx"):
                try:
                    import docx
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text + "\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"DOCX error: {str(e)}"}

        if resume_text and user_goal and result is None:
            try:
                result = analyze_resume(resume_text, user_goal)

                db = sessionlocal()
                try:
                    user = db.query(models.User).filter_by(email=session["user"]).first()
                    report = models.Report(
                        user_id=user.id,
                        resume_text=resume_text,
                        user_goal=user_goal,
                        result=json.dumps(result),
)
                    
                    db.add(report)
                    db.commit()
                finally:
                    db.close()
            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}

    return render_template(
        "dashboard.html",
        user=session["user"],
        result=result,
    )


@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    db = sessionlocal()
    try:
        user = db.query(models.User).filter_by(email=session["user"]).first()
        reports = db.query(models.Report).filter_by(user_id=user.id).all()

        parsed_reports = []
        for r in reports:
            try:
                parsed_result = json.loads(r.result)
            except Exception:
                parsed_result = {}
            parsed_reports.append({
                "resume": r.resume_text,
                "goal": r.user_goal,
                "result": parsed_result,
            })
    finally:
        db.close()

    return render_template("history.html", reports=parsed_reports)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)