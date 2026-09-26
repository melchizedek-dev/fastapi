from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

post: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "Python Tutorial: Working with JSON Data",
        "content": "In this video we will be learning how to work with JSON data in Python. We will cover how to parse JSON data, how to convert Python objects to JSON, and how to read and write JSON data to files.",
        "date_posted": "April 20, 2018"
    },
    {
        "id": 2,
        "author": "Corey Schafer",
        "title": "Python Tutorial: Sending HTTP Requests with the Requests Library",
        "content": "In this video we will be learning how to send HTTP requests using the requests library in Python. We will cover how to send GET and POST requests, how to handle responses, and how to work with JSON data.",
        "date_posted": "April 21, 2018"
    },
    {
        "id": 3,
        "author": "Corey Schafer",
        "title": "Python Tutorial: Working with APIs",
        "content": "In this video we will be learning how to work with APIs in Python. We will cover how to send requests to APIs, how to handle responses, and how to work with JSON data.",
        "date_posted": "April 22, 2018"
    },
    {
        "id": 4,
        "author": "Corey Schafer",
        "title": "Python Tutorial: Working with Databases",
        "content": "In this video we will be learning how to work with databases in Python. We will cover how to connect to databases, how to execute queries, and how to handle results.",
        "date_posted": "April 23, 2018"
    }
]

@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)
def home():
    return f"<h1>{post[0]["title"]}</h1>"

@app.get("/api/posts")
def get_posts():
    return post