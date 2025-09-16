# CineHub (Netflix-Style Platform)

## Project Overview
This final project is a streaming-like web application inspired by Netflix.  
Users can browse a catalog of movies with metadata such as **genre, cast, director, IMDb rating**, and more.  
The system supports a **watchlist** feature and links to **YouTube trailers** for each movie.

Demo video: [Watch here](https://youtu.be/Uxjzcv0l8dc?si=j8tfUqZy4BxAinei)

## Distinctiveness and Complexity
This project goes far beyond prior assignments:
- **Database-driven content**: Movies, genres, and metadata are dynamically retrieved from a backend.
- **Relational modeling**: Movies are linked to genres, actors, and directors.
- **Watchlist system**: Logged-in users can save movies to their personal watchlist.
- **IMDb rating integration**: Each movie displays rating data for better context.
- **YouTube trailer embedding**: Seamless video previews within the app.

This combination of features showcases significant technical depth and design creativity, well above a basic CRUD application.

## File Structure
- `cinehub/`: Django project configuration.
- `movies/`: Main app containing:
  - `models.py`: Defines Movies, Genres, Actors, Directors, and Watchlists.
  - `views.py`: Handles browsing, search, filtering, and watchlist logic.
  - `templates/`: UI templates for homepage, details, and watchlist.
- `static/`: CSS, images, and JS files for styling.

## How to Run
1. Install dependencies:
   ```bash
   pip install django requests
   ```
2. Apply migrations:
   ```bash
   python manage.py migrate
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/`.

## Future Improvements
- User reviews and rating system.
- Recommendation engine based on user watch history.
- Mobile-first responsive design.
