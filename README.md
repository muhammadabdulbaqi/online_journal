# Online Journal Application

A simple, modular web application for writing, viewing, editing, and deleting journal entries.  
Built using Python, Flask (for backend API), and Streamlit (for frontend interface).

## Features

- Add new journal entries
- View all entries with timestamps
- Edit or delete existing entries
- Streamlit-based UI that interacts with Flask API
- SQLite database for local storage
- Clean and modular project structure

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Flask REST API
- **Database**: SQLite (via `sqlite3` in Python)
- **Language**: Python 3

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/online_journal.git
cd online_journal
```

### 2. Set up virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask API
```bash
python -m api.routes
```

### 5. Run the Streamlit frontend
```bash
streamlit run app.py
```

## Folder Structure

```
online_journal/
├── app.py                 # Streamlit frontend
├── api/
│   ├── __init__.py
│   └── routes.py          # Flask API routes
├── database/
│   ├── __init__.py
│   └── db_utils.py        # SQLite functions (CRUD + init)
├── Planning/
│   ├── documentation.md   # Internal planning notes
│   └── requirements.pdf
├── requirements.txt
├── journal.db
└── .gitignore
```

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | /api/entries | List all entries |
| GET | /api/entries/<id> | Get single entry |
| POST | /api/entries | Create new entry |
| PUT | /api/entries/<id> | Update entry |
| DELETE | /api/entries/<id> | Delete entry |

## Planned Improvements

- Add search and filtering to journal view
- Sentiment analysis for each entry
- User authentication and private journals
- Deployment to a public platform (e.g. Streamlit Cloud, Fly.io)

## License

This project is open-source and free to use for learning and experimentation.