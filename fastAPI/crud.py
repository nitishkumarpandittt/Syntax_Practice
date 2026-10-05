from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

todos: dict[int, "Todo"] = {} # in-memory dict of todos

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    isCompleted: bool = False

#create - done
@app.post('/todos')
async def createTodo(todo: Todo):      # todo will work as request_body and Todo is the class
    if todo.id in todos:
        return "Todo already exists"
    todos[todo.id] = todo
    return todo

#read
@app.get('/todos')
async def getTodos():
    return list(todos.values())

@app.get('/todos/{todo_id}')
async def getTodoById(todo_id: int):
    todo = todos.get(todo_id)
    if not todo:
        return {"error": "no todo found"}
    return todo

#update
@app.put('/todos/{todo_id}')
async def updateTodo(todo_id: int, updated_todo: Todo):
    if todo_id not in todos:
        return {"error": "no todo found"}
    
    updated_todo.id = todo_id
    todos[todo_id] = updated_todo
    return updated_todo

#delete
@app.delete('/todos/{todo_id}')
async def deleteTodo(todo_id: int):
    todo = todos.get(todo_id)
    if not todo:
        return {"error": "no todo found"}
    todos.pop(todo_id)
    return {"message": "todo deleted successfully"}
