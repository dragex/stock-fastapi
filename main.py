from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Це схема даних. Вона каже API: "Чекай від користувача ці три поля"
class Stock(BaseModel):
    ticker: str
    price: float
    amount: int | None = None  # Це поле може бути порожнім

# 2. Головна сторінка
@app.get("/")
def read_root():
    return {"status": "API is working"}

# 3. Сторінка з інфою про тебе
@app.get("/info")
def get_info():
    return {"project": "Stock API", "author": "Roman"}

# 4. Маршрут для створення акції
@app.post("/stocks")
def create_stock(stock: Stock):
    return {"message": "Stock added", "data": stock}