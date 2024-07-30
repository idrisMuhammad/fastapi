from fastapi import FastAPI , Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],   
    allow_headers=["*"],

)

class Student(BaseModel):
    id:int
    name:str
    grade:int


students=[
        Student(id=1,name="Muhammad",grade=10),
        Student(id=2,name="Asmaa",grade=9),
        Student(id=3,name="Emy",grade=5),
    ]



@app.get("/students/")
def read_students():
    return students


@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    for index, student in enumerate(students):
        if student.id== student_id:
            students[index]=updated_student
            return updated_student

    return{"error":"Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message":"student deleted correctly"}
    return {"error":"student not found"}

        



 