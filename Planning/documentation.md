# 📓 Online Journal Application - Software Development Documentation

## 1. Requirements

### 1.1 Functional Requirements
- Users can create a new journal entry.
- Users can view a list of all journal entries.
- Users can view full content of a specific journal entry.
- Users can update an existing journal entry.
- Users can delete a journal entry.

### 1.2 Non-Functional Requirements
- Clean and simple user interface.
- Minimal or no CSS
- Local storage using SQLite.
- All operations should respond within 2 seconds.

### 1.3 Technology Stack
- **Backend**: Python (Flask)
- **Frontend**: Python (Streamlit) //for now
- **Database**: SQLite

### 1.4 System Architecture
- **Streamlit Client (UI)** ↔️ **Flask Server (Python)** ↔️ **SQLite Database**

## 2. Implementation Plan

### 2.1 Folder Structure

online_journal/
├── app.py                 # Streamlit frontend
├── api/                   
│   ├── __init__.py
│   └── routes.py          # Flask API routes
├── database/
│   ├── __init__.py
│   └── db_utils.py        # SQLite functions (table creation, CRUD)
├── requirements.txt
├── .gitignore
├── Planning/
│   ├── documentation.md   # Documentation containing information
│   └── requirements.pdf       


### 2.2 Data Schema (SQLite Table: entries)

| Column       | Type        | Description                 |
|--------------|-------------|-----------------------------|
| `id`         | INTEGER     | Primary Key, Auto-Increment |
| `title`      | TEXT        | Entry title                 |
| `content`    | TEXT        | Entry content               |
| `created_at` | TIMESTAMP   | Default to current time     |


### 2.3 API Routes (Flask)

| Method | Route                  | Description            |
|--------|------------------------|------------------------|
| GET    | `/api/entries`         | List all entries       |
| GET    | `/api/entries/<id>`    | Get single entry       |
| POST   | `/api/entries`         | Create entry           |
| PUT    | `/api/entries/<id>`    | Update entry           |
| DELETE | `/api/entries/<id>`    | Delete entry           |

### 2.4 Notes

Initial development starts from the database layer (db_utils.py).

Then API layer (routes.py), then UI layer (app.py).

Streamlit will use requests to talk to the Flask API.