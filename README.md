# 🚀 FastAPI Backend Project

## 📌 Overview

This is a backend project built using FastAPI with PostgreSQL, JWT authentication, and Alembic for database migrations.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vinaypatil99/fastapi-backend.git
cd <your-project-folder>
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Make sure your PostgreSQL database is running and update your database URL in config/settings file.

---

## 🔄 Alembic Migrations

### Initialize migrations (run only once)

```bash
alembic init migrations
```

### Create migration

```bash
alembic revision --autogenerate -m "your message"
```

### Apply migration

```bash
alembic upgrade head
```

---

## 🔐 Authentication

* Uses JWT (JSON Web Tokens)
* Token is required in headers:

```http
Authorization: Bearer <your_token>
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Once server is running:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## 📦 Generate Requirements File

If you install new packages:

```bash
pip freeze > requirements.txt
```

---

## 🧠 Notes

* Always use virtual environment
* Keep requirements.txt updated
* Run migrations after model changes
* Never commit secrets (use .env file)

---
