# AI-Powered Task Management System

## Overview

This project is a full-stack application designed to demonstrate the development of a secure, scalable backend system integrated with machine learning capabilities. The system allows users to manage tasks while automatically categorizing and prioritizing them using an ML model.

The primary focus of this project is on backend architecture, API design, and ML integration, with a lightweight frontend provided for demonstration purposes.

---

## Key Features

### Backend Features

* User authentication using JWT
* Role-based access control (user/admin ready structure)
* Secure password hashing (bcrypt)
* RESTful API design with versioning
* CRUD operations for task management
* Input validation using Pydantic
* Centralized error handling
* Structured logging with rotation
* Pagination support for APIs
* Modular and scalable project architecture

### Machine Learning Features

* Automatic task categorization using TF-IDF and Logistic Regression
* Real-time prediction during task creation
* Lightweight model loading for efficient inference
* Designed to be extendable to a dedicated ML microservice

### Frontend Features

* User registration and login
* JWT-based authentication handling
* Task creation and listing
* Displays ML-generated category and priority
* Responsive UI for demonstration

---

## System Architecture

Client (React Frontend)
→ FastAPI Backend (API Layer)
→ Service Layer (Business Logic + ML Integration)
→ Repository Layer (Database Access)
→ PostgreSQL Database

The ML model is integrated within the backend and is invoked during task creation.

---

## Backend Design (Focus Area)

The backend follows a clean and modular architecture:

* API Layer: Handles HTTP requests and responses
* Service Layer: Contains business logic and ML integration
* Repository Layer: Handles database operations
* Core Layer: Configuration, security, logging, and exception handling

This separation ensures scalability, maintainability, and ease of extension.

---

## Machine Learning Integration

A supervised learning approach is used for task categorization:

* Text is vectorized using TF-IDF
* Logistic Regression is used for classification
* Model is trained offline and saved as a serialized file
* At runtime, the model is loaded and used for prediction

This enables real-time intelligent behavior without affecting API performance.

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Passlib (bcrypt)
* Python-JOSE (JWT)

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Frontend

* React.js
* Axios

### DevOps

* Docker
* Docker Compose

---

## Setup Instructions

### Backend

1. Navigate to backend directory:

```
cd backend
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Train ML model:

```
python app/ml/train.py
```

4. Run server:

```
uvicorn app.main:app --reload
```

---

### Frontend

1. Navigate to frontend directory:

```
cd frontend
```

2. Install dependencies:

```
npm install
```

3. Run application:

```
npm start
```

---

## Docker Setup

To run the entire system using Docker:

```
docker-compose up --build
```

Services:

* Backend: http://localhost:8000
* Frontend: http://localhost:3000
* Database: PostgreSQL (port 5432)

---

## API Documentation

Available at:

```
http://localhost:8000/docs
```

---

## Future Enhancements

* Convert ML module into a separate microservice
* Add Redis caching for frequently accessed data
* Implement refresh tokens for authentication
* Add role-based admin controls
* Improve ML model with larger dataset and better feature engineering
* Add CI/CD pipeline for automated deployment

---

## Conclusion

This project demonstrates the ability to build a production-ready backend system with integrated machine learning capabilities. It focuses on clean architecture, scalability, and real-world engineering practices, making it suitable for deployment and further extension.
