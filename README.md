# Hospital FastAPI Project


# Overview

This project is a REST API built using FastAPI and Python to manage Doctors and Patients.


# Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

# Features

# Doctor APIs
* POST /doctors
* GET /doctors
* GET /doctors/{doctor_id}

# Patient APIs
* POST /patients
* GET /patients
* GET /patients/{patient_id}


# Setup Instructions

# 1. Install Requirements

pip install fastapi uvicorn email-validator

# 2. Run Server

uvicorn main:app --reload

# API Documentation

Open in browser:

http://127.0.0.1:8000/docs

# Validation Rules

* Email must be valid
* Age must be greater than 0
* Doctor not found
* Patient not found



