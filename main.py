from fastapi import FastAPI, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title":posts[0]["title"]})

@app.get("/posts/{post_id}", include_in_schema=False)
def post_details(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(request, "post.html", {"post":post, "title":title})
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def single_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.exception_handler(StarletteHTTPException)
def general_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (exception.detail if exception else "An error occured. Please check your request and try again!")
    if request.url.path.startswith("/api"):
        return JSONResponse(status_code=exception.status_code, content={"message": message})
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title":exception.status_code,
            "message":message
        },
        status_code=exception.status_code
    )

### RequestValidationError Handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )