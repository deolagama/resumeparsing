import fitz  
import re
def extract_text_from_pdf(file_path): 
    doc = fitz.open(file_path)  
    text = "" 
    for page in doc:
        text += page.get_text()
    return text


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-()]{8,}\d', text)
    return match.group(0) if match else "Not found"

def extract_skills(text):
    skill_keywords = ['python', 'java', 'sql', 'html', 'css', 'flask', 'c++', 'react']
    found = [skill for skill in skill_keywords if skill.lower() in text.lower()] 
    return found #The item you’re adding to the final list- is the first skill

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines:
        if len(line.split()) >= 2 and len(line) < 50:
            return line.strip()
    return "Not found"

def extract_education(text):
    edu_keywords = ['bachelor', 'master', 'b.tech', 'm.tech', 'b.sc', 'm.sc']
    for line in text.lower().split('\n'):
        if any(word in line for word in edu_keywords):
            return line.strip() 
    return "Not found"
