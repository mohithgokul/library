# 📚 Library Management System with Machine Learning

A Python-based **Library Management System** that integrates **database management** and **machine learning** to handle real-world library operations efficiently.

This project uses **SQLite** for persistent storage and implements a **content-based recommendation system** using **TF-IDF and cosine similarity**.

---

## 🚀 Features

### 🔐 Authentication
- Librarian login (default credentials)
- Member login using member ID and password
- Member self-registration

### 📖 Book Management (Librarian)
- Add new books
- Remove books
- Update book details
- Display all books
- Search books

### 👥 Member Management
- Register members
- View all members
- Remove members
- View individual member details

### 🔄 Issue & Return System
- Issue books to members
- Return books
- Automatic **availability tracking**
- Borrow history stored in database

### 💰 Fine Management
- 7-day borrowing period
- ₹5 per day fine after due date
- Fine calculation during return

### 🧠 Machine Learning Feature
- Book recommendation system
- Uses **TF-IDF + Cosine Similarity**
- Suggests similar books based on:
  - Title
  - Author
  - Genre

---

## 🛠️ Tech Stack

- **Python**
- **SQLite** (Database)
- **Pandas**
- **Scikit-learn**

---

## 📂 Project Structure

LibrarySystem/
│

├── main.py # Entry point (menus & flow)

├── library.py # Core logic (services)

├── database.py # Database operations

├── recommender.py # ML recommendation system

├── library.db # SQLite database (auto-created)

└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <https://github.com/mohithgokul/library>

cd library

pip install pandas scikit-learn

python main.py
