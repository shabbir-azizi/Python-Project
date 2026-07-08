from openai import OpenAI
import json

client = OpenAI()

def analyze_resume(resume_text,user_goal):
    prompt = f"""
You are a professional software engineer and hiring manager. 

Evaluate the resume based on the user's goal.

User goal:" {user_goal}"

STRICT RULES:



"""