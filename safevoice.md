# SafeVoice Backend Setup Instructions

This document summarizes the steps, decisions, commands, and architecture you have followed so far while building the SafeVoice backend using Flask, SQLAlchemy, and MVC principles.

---

## ✅ 1. Project Structure Created

```
backend-safevoice/
│
├── app/
│   ├── models/
│   ├── controllers/
│   ├── routes/
│   ├── utils/
│   │     └── serializer_mixin.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
├── .env
└── venv/
```

---

## ✅ 2. Virtual Environment Setup

**Commands used:**

```
python -m venv venv
venv\Scripts\activate      # On Windows
pip install flask sqlalchemy
pip freeze > requirements.txt
```

---

## ✅ 3. SQLAlchemy Models Created

### User model fields:

* id, username, email, password_hash, role, display_name, is_anonymous
* created_at, last_login

### Report model fields:

* id, user_id, abuse_type (Enum), description (Text), is_anonymous
* created_at, updated_at

### Message model fields:

* id, user_id, content (Text), receiver_type (Enum), is_anonymous
* is_read, created_at

---

## ✅ 4. Relationships Established

* User → Reports (one-to-many)
* User → Messages (one-to-many)

Each model uses `back_populates` to synchronize both sides of the relationship.

---

## ✅ 5. SerializerMixin Implemented

A reusable mixin placed in:

```
app/utils/serializer_mixin.py
```

Adds `.to_dict()` to all models for clean JSON serialization.

---

## ✅ 6. Git Commands Used So Far

```
git init
git add .
git commit -m "Add core models and serializer mixin"
git push origin main
```

---

This instructions document can be updated as you continue building the backend (controllers, routes, config, database setup, etc.).
