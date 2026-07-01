# AI Agent Development

## Week 1 - Study Buddy

This project implements a simple Study Buddy AI using LangChain and Google's Gemini model.

The application reads notes from a Markdown file and answers user questions based only on the content of those notes.

## Features

* Reads notes from a Markdown file (`my_notes.md`)
* Uses Gemini API through LangChain
* Answers questions based on provided notes
* Interactive command-line interface

## Project Structure

```text
AI_Agent_Development/
│
├── my_notes.md
├── study_buddy_week1.py
├── README.md
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mannate14/AI_Agent_Development.git
cd AI_Agent_Development
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install langchain python-dotenv langchain-google-genai
```

### 5. Create a .env File

Create a file named `.env` and add:

```text
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

### 6. Run the Application

```bash
python study_buddy_week1.py
```

## Testing

Example Questions:

* What is Artificial Intelligence?
* Summarize the notes.
* What are the applications of AI?

Example Question Outside Notes:

* Who is the President of India?

The Study Buddy should answer only using the provided notes and may not provide detailed information for topics not present in the notes.

## Author

Mannate Jain
NIT Silchar
