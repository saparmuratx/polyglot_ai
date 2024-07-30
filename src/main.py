from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_wardo():
    return "Herro Za Wardo"
