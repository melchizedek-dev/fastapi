from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

posts: list[dict] = [
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

@app.get("/",  include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts})
    

@app.get("/api/posts")
def get_posts():
    return posts