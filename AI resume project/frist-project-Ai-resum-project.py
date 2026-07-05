from flask import Flask, render_template, request, redirect, session
from db import base, engine, sessionlocal
import models
import PyPDF2
import docx
import json

app = Flask(__name__)


app.secret_key="secret123"

base.metadata.create_all(bind=engine)


@app.route('/')                                                

def home():
    return "App is runing"


if __name__ == '__main__':
    app.run(debug=True)
                                