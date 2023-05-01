from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

courses = []

class Course(BaseModel):
    id: int
    title: str
    description: str

@app.post("/courses/", response_model=Course)
def create_course(course: Course):
    courses.append(course)
    return course

@app.get("/courses/", response_model=List[Course])
def read_courses():
    return courses

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
