# Netflix Project (CineHub)

## Overview
This project is a Netflix-inspired streaming web application built with Django. It allows users to browse movies, view detailed information including IMDb rating, watch trailers via YouTube, and manage a personal watchlist. The goal of this project was to design a distinctive and complex web platform that demonstrates advanced use of Django beyond basic CRUD functionality.

## Distinctiveness and Complexity
This project goes well beyond the examples provided in CS50 Web:
- It implements **complex relationships** between models (Movies, Genres, Users, Watchlists).
- It integrates **YouTube trailers** for each movie.
- It provides a **user-specific watchlist**, demonstrating authentication, authorization, and database interactions.
- It uses **templates, static files, and media storage** to create a polished user experience similar to real-world streaming services.
- It includes **search and filtering features** to improve usability.
- Posters for movies are **added manually via the Django Admin interface**, which demonstrates use of Django's built-in administration tools.

These features demonstrate both distinctiveness (not a simple blog or e-commerce site) and complexity (multiple apps, models, authentication, media handling).

## File Structure and Explanation
- **netflix/** - Main Django project configuration (settings, urls, wsgi).
- **movies/** - Core app for the platform.
  - `models.py` - Defines Movie, Genre, and Watchlist models.
  - `views.py` - Contains view logic for displaying movies, details, and user-specific lists.
  - `templates/movies/` - HTML templates for the UI (homepage, details page, watchlist).
  - `urls.py` - Routing for the movies app.
- **static/** - CSS, JS, and image assets.
- **media/** - Movie poster images uploaded manually through the Django Admin.
- **requirements.txt** - Python dependencies (Django, etc.).
- **manage.py** - Django project management script.
- **db.sqlite3** - Local SQLite database.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/matin1385-tech/netflix-project.git
   cd netflix-project
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on macOS/Linux
   venv\Scripts\activate    # on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open `http://127.0.0.1:8000/` in your browser.

## Future Improvements
- Add user reviews and ratings for movies.
- Implement recommendation system based on watch history.
- Create responsive mobile-friendly design.
- Enhance search with autocomplete and filtering by multiple fields.

## Demo
You can watch a demo of the project here:  
[Demo Video](https://youtu.be/CNtvks7O3cQ?si=mMTFjv43xX1G9HuQ)

## Credits
Developed as a final project for **CS50's Web Programming with Python and JavaScript**.
