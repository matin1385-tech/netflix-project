# Netflix Django Project 🎬

A Netflix-like movie web application built with **Django** and **Bootstrap 5**.  
Users can browse movies, view details, watch trailers, and manage a personal watchlist.

---

## Features

- **Movie Catalog**:
  - Title, Year, Genre, Description
  - Poster image
  - IMDB rating
  - Actors and Directors
  - Trailer modal

- **User Authentication**:
  - Register / Login / Logout
  - Add movies to watchlist (requires login)
  
- **Responsive Design**:
  - Bootstrap 5 for mobile-first layout
  - Modern UI with cards, modals, and buttons

- **Admin Panel**:
  - Full CRUD access to movies, actors, and directors
  - Easy management of watchlists

---

## 🗂️ Project Structure
│   .gitattributes
│   .gitignore
│   db.sqlite3
│   manage.py
│   README.md
│   requirements.txt
│
├───finalproject
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
├───media
│   ├───netflix
│   │   └───images
└───netflix
    │   admin.py
    │   apps.py
    │   forms.py
    │   models.py
    │   tests.py
    │   urls.py
    │   views.py
    │   __init__.py
    ├───static
    │   └───netflix
    │       │   scripts.js
    │       │   style.css
    │       │
    │       └───images
    ├───templates
    │   └───netflix
    │           index.html
    │           layout.html
    │           login.html
    │           movie_detail.html
    │           register.html
    │           watchlist.html

