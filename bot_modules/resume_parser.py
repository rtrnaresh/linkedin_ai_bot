import re
import pdfplumber

# ✅ Load text from your resume
def extract_text_from_resume(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    return text

# ✅ Extract skills based on known tech/terms
def extract_skills(text):
    keywords = [
        "Python", "Java", "HTML", "CSS", "JavaScript", "SQL", "MongoDB", "AWS",
        "CI/CD", "Jenkins", "Docker", "DevOps", "DBMS", "OOPS", "AI", "Machine Learning",
        "Cloud", "Prompt Engineering", "Data Structures", "Algorithms", "Web Development",
        "Microservices", "Spring Boot", "IoT"
    ]
    found = [kw for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE)]
    return list(set(found))

# ✅ Extract job titles from resume
def extract_roles(text):
    titles = [
        "Software Engineer", "AI Engineer", "Full Stack Developer", "DevOps Engineer",
        "Cloud Engineer", "Python Developer", "Java Developer", "Data Analyst", "ML Engineer"
    ]
    found = [role for role in titles if role.lower() in text.lower()]
    return list(set(found))

# ✅ Extract and summarize
def parse_resume(file_path):
    text = extract_text_from_resume(file_path)
    skills = extract_skills(text)
    roles = extract_roles(text)
    return {
        "skills": skills,
        "roles": roles,
        "raw": text
    }

# 🧪 Example use (for local testing only)
if __name__ == "__main__":
    parsed = parse_resume("Naresh Resume.pdf")
    print("Extracted Skills:", parsed["skills"])
    print("Suggested Job Titles:", parsed["roles"])