# Expense Tracker

A simple **Django-based web application** to help users track their personal expenses and incomes.

This project uses Python and the Django web framework to create, view, and manage expense records. It allows you to record financial transactions and view summaries of your spending over time.

---

## 🧠 Features

✔️ Add and record expenses  
✔️ Categorize transactions (e.g., Food, Transport, Bills)  
✔️ View transaction history  
✔️ See totals and summaries of expenses/income  
✔️ Simple web interface for managing personal finances

*(You can extend it with charts, filters, authentication, reports, etc.)*

---

## 🛠️ Tech Stack

| Technology | Version |
|------------|---------|
| Python     | 3.x     |
| Django     | 4.x     |
| Database   | SQLite (default for Django) |

---

## 🚀 Setup & Installation

### 1. Clone the repository

git clone https://github.com/jaisurya-d/expense_tracker.git
cd expense_tracker

### 2. Create & activate a virtual environment

# Linux / macOS

  python3 -m venv venv
  source venv/bin/activate

# Windows (PowerShell)

  python -m venv venv
  venv\Scripts\Activate

### 3. Install dependencies

pip install django

### 🏁 Running the Application
python manage.py migrate
python manage.py runserver
Now open in a web browser: http://127.0.0.1:8000
