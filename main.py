from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API to do application")

@app.get("/")
def main():
  return {"message":"this is to do app"}

class Todo(BaseModel):
  name: str
  due: str
  desc: str

store = []

@app.post("/todo")
async def post_todo(todo: Todo):
  store.append(todo)
  return {
    "message": "todo created",
    "data": todo
  }

@app.get("/todo", response_model=List[Todo])
async def get_all_todo():
  return store

@app.get("/todo/{id}")
async def get_todo(id: int):
  try:
    return store[id]
  except:
    raise HTTPException(status_code=404, detail="Not found")

@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
  try:
    store[id] = todo
    return {
      "message": "todo updated",
      "data": todo
    }
  except:
    raise HTTPException(status_code=404, detail="Not found")

@app.delete("/todo/{id}")
async def delete_todo(id: int, todo: Todo):
  try:
    obj = store[id]
    store.pop[id]
    return {
      "message": "todo deleted",
      "data": obj
    }
  except:
    raise HTTPException(status_code=404, detail="Not found")
