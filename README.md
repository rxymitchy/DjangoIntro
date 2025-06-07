# Django Blog Project

This repository contains my first blog application built with **Django**, a powerful Python web framework.

---

## 📝 Project Overview

A basic blog platform featuring:

- User authentication and registration
- Creating, editing, and deleting blog posts
- Media file management for blog content (images, videos)
- Simple and clean UI powered by Django templates
- SQLite database for development and testing

---

## 📂 Repository Structure

| Folder/File        | Description                        |
|--------------------|----------------------------------|
| `blog/`            | Blog app containing models, views, and templates |
| `first_django_project/` | Django project configuration files          |
| `media/`           | Folder for uploaded media files  |
| `users/`           | User authentication and management app  |
| `.gitignore`       | Git ignore file                   |
| `db.sqlite3`       | SQLite database file              |
| `manage.py`        | Django management script          |

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog


2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Open your browser and visit** `http://127.0.0.1:8000/` to see the blog.

---

## 📦 Technologies Used

* Python 3.x
* Django 4.x
* SQLite (default development database)
* HTML, CSS for frontend templates

---

## 📄 License

This project is open-source under the MIT License.

---

## 👤 Author

**rxymitchy**

* GitHub: [https://github.com/rxymitchy](https://github.com/rxymitchy)

---

*This Django blog project is a great starting point for beginners to learn full-stack web development with Python.*
