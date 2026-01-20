from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/add")
def add(a: int, b: int):
    """2つの整数を加算して結果を返すエンドポイント"""
    return {"result": a + b}
