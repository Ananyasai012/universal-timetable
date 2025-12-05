from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Input model
class TimetableInput(BaseModel):
    teachers: List[str]
    subjects: List[str]
    classes: List[str]
    periods_per_day: int

# Home route
@app.get("/")
def home():
    return {"message": "Universal Timetable API is running!"}

# POST endpoint to generate timetable
@app.post("/generate-timetable")
def generate_timetable(data: TimetableInput):
    timetable = {}
    for cls in data.classes:
        timetable[cls] = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            daily_periods = []
            for i in range(data.periods_per_day):
                # simple round-robin assignment
                teacher = data.teachers[i % len(data.teachers)]
                subject = data.subjects[i % len(data.subjects)]
                daily_periods.append(f"{subject} - {teacher}")
            timetable[cls].append({day: daily_periods})
    return {"timetable": timetable}
