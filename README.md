# 🚀 AWS Blog Summarizer

## Overview
AWS Blog Summarizer is a Streamlit-based web application that scrapes AWS Big Data blogs, fetches their content, and generates concise summaries using the DeepSeek LLM model.

## Features
- ✅ Fetches the latest AWS Big Data blog posts
- ✅ Extracts and summarizes blog content using DeepSeek LLM
- ✅ Displays key takeaways in a structured bullet-point format
- ✅ Simple UI powered by Streamlit

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/aws-blog-summarizer.git
cd aws-blog-summarizer
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # For macOS/Linux
# or
.venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Ollama (for DeepSeek Model)
Ensure you have [Ollama](https://ollama.ai/) installed and running. Then, run the following command to load the **DeepSeek** model:
```bash
ollama run deepseek-r1:1.5b
```

## 🚀 Running the Application
```bash
streamlit run app/ui.py
```
This will start a local Streamlit server, and you can access the app in your browser.

## 🌍 Deploying on GitHub

### 1. Initialize Git
```bash
git init
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/aws-blog-summarizer.git
git branch -M main
```

### 2. Add & Commit Changes
```bash
git add .
git commit -m "Initial commit"
```

### 3. Push to GitHub
```bash
git push origin main
```

## 🛠 Troubleshooting
- If `git push` fails, use:
  ```bash
  git remote set-url origin https://github.com/YOUR_GITHUB_USERNAME/aws-blog-summarizer.git
  git push origin main --force
  ```
- If you face permission issues, use a **GitHub Personal Access Token (PAT)** instead of your password.

## 📜 License
This project is open-source under the **MIT License**. Feel free to modify and contribute!

