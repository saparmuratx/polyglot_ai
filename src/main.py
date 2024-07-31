from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")


@app.get("/")
def hello_wardo():
    return "Herro Za Wardo"


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/foo", response_class=HTMLResponse)
def foo(request: Request):
    return templates.TemplateResponse("foo.html", {"request": request})


@app.get("/bar", response_class=HTMLResponse)
def bar(request: Request):
    return templates.TemplateResponse("bar.html", {"request": request})
