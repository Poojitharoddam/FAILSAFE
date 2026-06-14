from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

# ==========================
# In-Memory Student Storage
# ==========================

students_db = []

# ==========================
# Student Model
# ==========================

class Student(BaseModel):
    id: int
    name: str
    age: int
    attendance: float
    marks: float


# ==========================
# Get All Students
# ==========================

@router.get("/")
def get_students():

    return {
        "count": len(students_db),
        "students": students_db
    }


# ==========================
# Add Student
# ==========================

@router.post("/")
def add_student(student: Student):

    students_db.append(student.dict())

    return {
        "message": "Student Added Successfully",
        "student": student
    }


# ==========================
# Get Student By ID
# ==========================

@router.get("/{student_id}")
def get_student(student_id: int):

    for student in students_db:

        if student["id"] == student_id:

            return student

    return {
        "message": "Student Not Found"
    }


# ==========================
# Delete Student
# ==========================

@router.delete("/{student_id}")
def delete_student(student_id: int):

    global students_db

    students_db = [
        student
        for student in students_db
        if student["id"] != student_id
    ]

    return {
        "message": "Student Deleted Successfully"
    }