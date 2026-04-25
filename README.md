# 🔗 Persistent URL Shortener with Automated TTL

A lightweight Python-based URL shortener that utilizes **SQLite** for data persistence and a decoupled **Cron Job** for automated link expiration.

## 🚀 Key Features
* **Persistent Storage:** Uses SQLite to ensure shortened URLs survive application restarts.
* **Decoupled Maintenance:** Background "Janitor" script handles data cleanup without impacting user performance.
* **Time-To-Live (TTL):** Automated expiration logic that purges links older than 3 hours.
* **Security-First:** Implements parameterized SQL queries to prevent SQL Injection attacks.

## 🏗️ System Architecture
The system is divided into two primary components to ensure **Separation of Concerns**:

1.  **Main Application (`app.py`):** Handles URL shortening, unique code generation, and redirection lookups.
2.  **Janitor Script (`janitor.py`):** A standalone maintenance utility that purges expired records.

## 🛠️ Setup & Installation

### 1. Prerequisites
* Python 3.x
* SQLite3 (Built-in with Python)

### 2. Initialization
Run the main application to initialize the database and shorten your first URL:
```bash
python app.py
