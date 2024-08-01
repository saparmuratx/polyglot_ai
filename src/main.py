from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import models, schemas, crud, utils

from .database import engine, get_db

from .settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="src/templates")

models.Base.metadata.create_all(bind=engine)


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


@app.post("/translate", response_model=schemas.TaskResponse)
async def translate(
    request: schemas.TranslationRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    task = crud.create_translation_task(db, request.text, request.languages)

    background_tasks.add_task(utils.perform_translation())

    return task


@app.get("/translate/{task_id}", response_model=schemas.TranslationStatus)
async def translate_get(task_id: int, db: Session = Depends(get_db)):
    return crud.get_translation_task(db, task_id)
