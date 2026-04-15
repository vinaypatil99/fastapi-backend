# 🚀 FastAPI Backend (RBAC Enabled)

## 📌 Overview

This is a backend project built using FastAPI with authentication, role-based access control (RBAC), and task management features.

---

## 🛠 Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic (migrations)
* JWT Authentication
* Pydantic Settings

---

## 🔐 Authentication & Authorization

### ✅ JWT Authentication

* Users can register and login
* JWT token is generated on login
* Token contains:

  * User ID
  * Role (admin/user)
  * Expiry

---

### 🔒 Role-Based Access Control (RBAC)

The system supports two roles:

* **user**
* **admin**

#### 🔹 Features:

* Role stored in database
* Role included in JWT payload
* Protected routes using dependency-based authorization

---

## 👑 Admin Features

Admin-only APIs:

* `GET /admin/users` → Get all users
* `GET /admin/tasks` → Get all tasks
* `GET /admin/stats` → Dashboard stats

🔐 Protected using RBAC:
Only users with role = `admin` can access these endpoints.

---

## 👤 User Features

* Register new user
* Login user
* Create tasks
* Manage own tasks

---

## 🔄 API Endpoints

### 🔓 Public Routes

* `POST /register` → Register user
* `POST /login` → Login user

---

### 🔐 Protected Routes

* Requires JWT token in header:

```
Authorization: Bearer <token>
```

---

### 👑 Admin Routes

* `GET /admin/users`
* `GET /admin/tasks`
* `GET /admin/stats`

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/vinaypatil99/fastapi-backend.git
cd fastapi-backend
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create `.env` file:

```
DB_CONNECTION=postgresql://postgres:password@localhost:5432/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_SECONDS=30
```

---

### 4️⃣ Run Migrations

```bash
alembic upgrade head
```

---

### 5️⃣ Start Server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Open Swagger UI

```
http://localhost:8000/docs
```

---

## 🧠 Architecture

```
src/
 ├── users/
 ├── tasks/
 ├── admin/
 ├── utils/
```

* `users` → user management
* `tasks` → task management
* `admin` → admin-only routes
* `utils` → helpers, DB, settings

---

## 🔐 Security Features

* Password hashing using Argon2
* JWT-based authentication
* Role-based authorization (RBAC)
* Protected admin routes
* Secure token validation

---

