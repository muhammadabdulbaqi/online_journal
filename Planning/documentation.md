# 📓 Online Journal Application - Software Development Documentation
  
## 1. Requirements

### 1.1 Functional Requirements
- Users can create a new journal entry.
- Users can view a list of all journal entries.
- Users can view full content of a specific journal entry.
- Users can update an existing journal entry.
- Users can delete a journal entry.

### 1.2 Non-Functional Requirements
- Activate env: venv\Scripts\activate    
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

## 3. Development Progress

### 3.1 Completed

- [x] Set up virtual environment and installed dependencies (Flask, Streamlit)
- [x] Defined folder structure
- [x] Created and tested database logic in `db_utils.py`
- [x] Verified CRUD operations using `test_db_utils.py` (modular test functions)

### 3.2 In Progress — Flask API (`routes.py`)

- Created Flask server inside `api/routes.py`
- Defined all API endpoints:
  - `GET /api/entries`
  - `GET /api/entries/<id>`
  - `POST /api/entries`
  - `PUT /api/entries/<id>`
  - `DELETE /api/entries/<id>`
- Each route uses functions from `db_utils.py`
- Returns JSON responses and appropriate HTTP status codes
- Currently testing endpoints independently with Postman

---

## 4. Testing API Routes

### 🔧 How to Run the Flask API

From the project root:

```bash
python -m api.routes
```

### ✅ Test Routes Using Postman

| Method | Endpoint | Description | Notes |
| ------ | -------- | ----------- | ----- |
| GET | `/api/entries` | List all entries | Returns array of entries |
| POST | `/api/entries` | Create a new entry | Requires JSON body |
| GET | `/api/entries/<id>` | Fetch a single entry by ID | Returns entry object |
| PUT | `/api/entries/<id>` | Update an existing entry | Requires JSON body |
| DELETE | `/api/entries/<id>` | Delete an entry by ID | Returns 204 No Content |

### 🔍 Request Body Examples

#### 📝 POST (Create)
```json
{
  "title": "My First Entry",
  "content": "Testing the API with Postman"
}
```

#### ✏️ PUT (Update)
```json
{
  "title": "Updated Title",
  "content": "Updated content goes here"
}
```

### 🧪 What to Verify

✅ Correct HTTP status codes:
- 200 OK – Success for GET, PUT
- 201 Created – Entry was successfully added
- 204 No Content – Entry successfully deleted
- 400 Bad Request – Missing required fields
- 404 Not Found – Entry not found (invalid ID)

✅ JSON response formatting

✅ Clear error messages when inputs are missing or incorrect

✅ That entries are:
- Successfully created
- Properly updated
- Fully deleted

## 5. Upcoming Tasks

### 📌 5.1 Initialize README.md
We will begin drafting a GitHub-friendly README file including:

✅ Project description  
✅ Technology stack  
✅ How to run the app (setup + usage)  
✅ API route documentation  
✅ Screenshots (once frontend is ready)  
✅ (Optional) Deployment instructions (e.g., Render, Railway)

### 📌 5.2 Phase 6 — Build Streamlit UI (app.py)
Planned goals for the UI layer:

🔹 Display a list of journal entries (fetched from the API)  
🔹 Add a new entry via Streamlit form  
🔹 Edit or delete entries using buttons  
🔹 Use the requests library to talk to Flask  
🔹 Keep UI logic modular and clean  
🔹 Ensure full-stack (UI → API → DB) functionality is working