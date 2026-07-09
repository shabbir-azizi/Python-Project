from openai import OpenAI
import json

client = OpenAI()

def analyze_resume(resume_text,user_goal):
    prompt = f"""
You are a professional software engineer and hiring manager. 

Evaluate the resume based on the user's goal.

User goal:" {user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools [excel for backend,etc]
- Idsentify real gaps
- Generate roadmap only for missing fields
- make sure to provide a clear and concise summary of the resume's strengths and weaknesses in relation to the user's goal.M    
- Make output DIFFERENT based on goal 


Return only JSON:
{{
"skills":[],
"missing_skills":[],
roadmap":[],

}}


"""