from fastapi import FastAPI
from app.scraper import fetch_aws_blogs
from app.summarizer import summarize_blog

app = FastAPI()

@app.get("/blogs")
def get_blogs():
    return fetch_aws_blogs()

@app.get("/summarize")
def summarize(blog_url: str):
    content = fetch_blog_content(blog_url)
    return summarize_blog(content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)