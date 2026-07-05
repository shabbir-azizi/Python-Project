from flask import Flask, render_template, request, redirect, session
from db import base, engine, sessionlocal
import models

app = Flask(__name__)


@app.route('/')                                                

def home():
    return "App is runing"


if __name__ == '__main__':
    app.run(debug=True)
                                