# Resume Parser🕵️
The project aims to develop a machine learning-based solution for automated resume detection and extraction. With the increasing volume of job applications, it becomes challenging for recruiters to manually review and extract information from each resume. This project seeks to streamline and expedite the resume screening process by leveraging machine learning algorithms.

The system will utilize state-of-the-art natural language processing (NLP) techniques and machine learning models to analyze and extract relevant information from resumes using SpaCy, Scikit-Learn etc.

## 👨‍💼🤖 Don't believe us?

🤣 We could tell you about how Resume Miner helped a company find their next CEO, but that would just be bragging. Instead, here are some more modest examples:

👨‍💼 **Hiring manager** : "I used to spend hours reading through resumes, but now with Resume Miner, I can find the perfect candidate in just minutes! It's like having a personal assistant that never sleeps."

👩‍💻 **Recruiter**: "I love using Resume Miner to find top-notch candidates. It's like a metal detector for resumes - it helps me uncover hidden gems that I might have missed otherwise."

🕵️‍♂️ **Detective**: "Okay, so I'm not actually a detective, but sometimes it feels like it when I'm trying to find the right candidate for a job. With Resume Miner, it's like I have X-ray vision - I can see right through a resume and find the information I need."

See? Even fictional characters can benefit from Resume Miner! Give it a try and see for yourself. 😉

## Clone Repo And use it
* Clone resume_miner repo using below command
```git
git clone https://github.com/SatyaTheG/Resume_Parser.git
```

## Installation Steps

```bash
  pip install -r requirements.txt
```

## Execution Steps

=> Just locate your Command Prompt or Powershell to Project Folder

=> Run the following command to activate the flask API server

```bash
  python app.py
```

=> Here we have two endpoints "/resumeparser" and "/resumedetection".

=> "/resumeparser" is directly extracting information from PDF file without ensuring that the given PDF file is RESUME or not.

=> "/resumedetection" is checking first that the given PDF file is RESUME or not and after that if it is then it will start to extract information from it else it will simply display that the given PDF file is not RESUME.

=> To use the service of API, you have give the following inputs to PostMan...

1. Create a new request with POST method and http://127.0.0.1:5000/resumedetection

2. In authorization tab, give username and password credentials which are defined in .env file of the project.

3. In Body tab move to form-data tab, enter key as "filePath" and select type of input as File and select file from values column.

4. Also give the information of your desired information like name, email, phone or skills in array withe key value "extractFields" and select type of input as Text and give that array into Values column as ["name", "email", "phone","skills"] if you want to have only name , email , phone and skills from the uploaded PDF file.

5. If you want to have all information from PDF file then no need to follow step 4.
