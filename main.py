from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List

app=FastAPI()

@app.get("/")
def home():
    return {"message" : "API RUNNING SUCCESSFULLY!"}

# Database
doctors=[]
patients=[]
doctor_id_counter=1
patient_id_counter=1

# Doctor Model
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Doctor(DoctorCreate):
    id: int


# Patient Model
class PatientCreate(BaseModel):
    name: str
    age: int = Field(..., gt=0)  # age > 0 validation
    phone: str

class Patient(PatientCreate):
    id: int

# DOCTOR APIS

@app.post("/doctors", response_model=Doctor)
def create_doctor(doctor: DoctorCreate):
    global doctor_id_counter

    new_doctor = {
        "id": doctor_id_counter,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)
    doctor_id_counter += 1
    return new_doctor


@app.get("/doctors", response_model=List[Doctor])
def get_doctors():
    return doctors

@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(status_code=404, detail="Doctor not found")

# PATIENT APIS

@app.post("/patients", response_model=Patient)
def create_patient(patient: PatientCreate):
    global patient_id_counter

    new_patient = {
        "id": patient_id_counter,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }
    patients.append(new_patient)
    patient_id_counter += 1
    return new_patient


@app.get("/patients", response_model=List[Patient])
def get_patients():
    return patients

@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")