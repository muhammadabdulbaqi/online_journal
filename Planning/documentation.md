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
- **Frontend**: HTML, CSS (Jinja2 templating)
- **Database**: SQLite

### 1.4 System Architecture
- **Client (Browser)** ↔️ **Flask Server (Python)** ↔️ **SQLite Database**

---
(Optional Phase 2: Add a Flask API between Streamlit and SQLite)