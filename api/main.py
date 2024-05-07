from fastapi import FastAPI
from .routes.todo_router import router as todo_router

app = FastAPI(title="Todo API", version="1.0.0", description="An API to manage to-do lists")

# Include routers from the routes module
app.include_router(todo_router, prefix="/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API powered by FastAPI"}
