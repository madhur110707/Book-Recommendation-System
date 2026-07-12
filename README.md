# 📚 Book Recommendation System

A Machine Learning-based Book Recommendation System that suggests books similar to the one selected by the user using **Collaborative Filtering (K-Nearest Neighbors)**. The project uses **FastAPI** as the backend, **MySQL** for storing book information, and will have a responsive **HTML, CSS, and JavaScript** frontend.

---

## 🚀 Features

- 🔍 Search books with live suggestions
- 📖 View complete book details
- 🤖 Get personalized book recommendations
- ⭐ Browse popular books
- 🗄️ MySQL database integration
- ⚡ FastAPI REST API backend
- 🎨 Responsive frontend (Under Development)

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- MySQL
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Frontend
- HTML
- CSS
- JavaScript

### Database
- MySQL

### Machine Learning
- Collaborative Filtering
- K-Nearest Neighbors (KNN)

### Version Control
- Git
- GitHub

---

# 📂 Project Structure

```
Book-Recommendation-System/
│
├── backend/
│   ├── artifacts/
│   │   ├── model.pkl
│   │   ├── books_name.pkl
│   │   ├── book_pivot.pkl
│   │   └── final_rating.pkl
│   │
│   ├── database/
│   │   ├── db_connection.py
│   │   ├── fetch_books.py
│   │   └── insert_books.py
│   │
│   ├── main.py
│   ├── recommendation.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── notebooks/
│   └── Book Recommender.ipynb
│
├── Table_Creation.sql
├── README.md
└── .gitignore
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Health Check |
| GET | `/popular-books` | Returns popular books |
| GET | `/search?query=` | Returns search suggestions |
| GET | `/book/{title}` | Returns book details |
| GET | `/recommend/{title}` | Returns recommended books |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/madhur110707/Book-Recommendation-System.git
```

---

## 2. Navigate into the project

```bash
cd Book-Recommendation-System
```

---

## 3. Create a virtual environment

```bash
python -m venv .venv
```

---

## 4. Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 5. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 6. Configure MySQL

- Create a MySQL database.
- Run `Table_Creation.sql`.
- Update the database credentials in:

```
backend/database/db_connection.py
```

---

## 7. Start the FastAPI server

```bash
cd backend

python -m uvicorn main:app --reload
```

---

## 8. Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📷 Screenshots

Coming Soon...

---

# 🔮 Future Improvements

- User authentication
- User ratings and reviews
- Personalized recommendations
- Genre-based filtering
- Recently viewed books
- Dark mode
- Book wishlist
- Deployment on Render/AWS

---

# 👨‍💻 Author

**T. S. Kalyana Madhur**

GitHub:
https://github.com/madhur110707

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.