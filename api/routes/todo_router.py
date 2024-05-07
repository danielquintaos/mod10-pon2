from fastapi import APIRouter, HTTPException, status
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Mock database
todos = [
    {"id": "1", "title": "Grocery Shopping", "description": "Buy milk, eggs, and bread"},
    {"id": "2", "title": "Workout", "description": "Go for a 30-minute run"}
]

# Pydantic models
class Todo(BaseModel):
    id: str
    title: str
    description: str

class TodoCreate(BaseModel):
    title: str
    description: str

# Routes
@router.get("/", response_model=List[Todo])
async def list_todos():
    return todos

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    new_todo = {"id": str(len(todos) + 1), **todo.dict()}
    todos.append(new_todo)
    return new_todo

@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, todo: TodoCreate):
    for index, current_todo in enumerate(todos):
        if current_todo["id"] == todo_id:
            updated_todo = {**current_todo, **todo.dict()}
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str):
    global todos
    for index, current_todo in enumerate(todos):
        if current_todo["id"] == todo_id:
            todos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")
