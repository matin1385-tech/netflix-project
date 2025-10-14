# MyFlix (Netflix-style Mini Streaming Catalog)

MyFlix is a Django-based web app inspired by Netflix that lets users register/login, browse a catalog of movies, view rich details (poster, genre, IMDb rating, actors, directors), play trailers in a modal, and manage a personal Watchlist. The app is server-rendered with Django templates, styled with Bootstrap, and handles uploaded media via Django's ImageField.

The project models core streaming concepts: movies with many-to-many relations to actors and directors, per-user watchlists, and a clean UI for discovery and detail views. It integrates Django's authentication, form validation, media handling, URL routing, and the admin site into a cohesive product.

## Distinctiveness and Complexity

This capstone differs meaningfully from the course's earlier assignments (Wiki, Commerce, Mail, Network) in both domain and implementation:

- Rich domain modeling for a streaming catalog
  - Movie has many-to-many relations to both Actor and Director, enabling richer metadata and queries than the simple CRUD patterns of earlier psets.
  - Media handling: Movie.poster uses Django's ImageField with a MEDIA pipeline and template fallback logic.

- Personalized features
  - Per-user Watchlist modeled as a separate table linked to both User and Movie, with add/remove flows and access restricted to authenticated users.

- UX and front-end behavior
  - Trailer playback via a Bootstrap modal. A small JS utility derives an embeddable URL from a standard YouTube link, updates the modal title dynamically, and stops playback when the modal closes.

- Cohesive integration of Django subsystems
  - Authentication (register/login/logout), CSRF-protected forms, server-rendered templates, static and media files, admin customization, and conditional URL patterns for serving media in development.

Compared to prior assignments, the app's data model (two many-to-many relations, explicit join model for watchlists, image uploads) and user-facing workflows (personalized watchlist and trailer modal behavior) go beyond the CRUD and messaging patterns in earlier problems, requiring coordination of models, permissions, forms, template logic, static/media assets, and the admin interface.

## File-by-File Write-Up (only files to which I contributed code)

### Project config
- **finalproject/settings.py**
  - INSTALLED_APPS includes "netflix".
  - DEBUG=True for development; SQLite used by default (db.sqlite3).
  - Templates: APP_DIRS=True so app templates resolve under templates/netflix/.
  - Static/Media: STATIC_URL="static/"; MEDIA_URL="/media/"; MEDIA_ROOT = BASE_DIR / "media" to support ImageField uploads for posters.
  - Messages/auth middleware and context processors enabled (used by login/registration flows).
  - Note: This is development-only config; the SECRET_KEY here is not for production.

- **finalproject/urls.py**
  - urlpatterns include:
    - path('admin/', admin.site.urls) to expose Django Admin.
    - path('', include('netflix.urls')) to mount the app's routes at the site root.

- **netflix/admin.py**
  - Registers Movie in the Django admin with a custom ModelAdmin:
    - list_display = ('title', 'year', 'genre')
    - search_fields = ('title', 'genre')
  - This improves content management for seeding and maintaining the catalog.

- **netflix/forms.py**
  - RegisterForm: Extends UserCreationForm and requires email; used to create and auto-login new users.
  - LoginForm: Username/password form with PasswordInput widget.

- **netflix/models.py**
  - Actor: name and optional birt### App (Django)
h_year; __str__ for readability.
  - Director: similar to Actor; separate model to accurately model roles.
  - Movie: title, description, poster (ImageField uploads to netflix/images/), year, genre, optional trailer_url and imdb_rating; many-to-many relations to Actor and Director.
  - Watchlist: explicit model linking User to Movie; views use get_or_create to prevent duplicates.

- **netflix/views.py**
  - index: Lists all movies (home page).
  - movie_detail: Detailed page with poster, genre, rating, actors, directors, and trailer button.
  - watchlist (login_required): Renders the authenticated user's watchlist.
  - add_to_watchlist (login_required): Adds a movie for the current user (idempotent via get_or_create).
  - remove_from_watchlist (login_required): Removes a movie from the current user's watchlist.
  - register_view: Handles registration with RegisterForm; logs the user in on success.
  - login_view: Authenticates via LoginForm; uses Django messages for invalid credentials.
  - logout_view: Logs out and redirects to the index.

- **netflix/urls.py**
  - Route definitions for index, movie_detail, watchlist, add/remove, register, login, and logout.
  - When settings.DEBUG is True, appends static() to serve MEDIA files for poster display during development.

### Templates (Django)
- **templates/netflix/layout.html**
  - Base layout with Bootstrap CSS/JS (CDN), nav bar with auth-aware links (Watchlist vs Login/Register), and inclusion of static assets (style.css, scripts.js).

- **templates/netflix/index.html**
  - Grid of movie cards with poster (fallback to a default image), title, and a Details button.

- **templates/netflix/movie_detail.html**
  - Rich details: title, year, genre, description, IMDb rating, actors, directors.
  - Auth-aware "Add to Watchlist" button.
  - "Play Trailer" opens a Bootstrap modal with a responsive 16:9 iframe.

- **templates/netflix/login.html**
  - Login form with inline error messages; link to registration page.

- **templates/netflix/register.html**
  - Registration form (username, email, password1, password2).

- **templates/netflix/watchlist.html**
  - Displays the authenticated user's watchlist as cards with poster, Details, and Remove actions.

### Static
- **static/netflix/scripts.js**
  - Listens to Bootstrap modal events; transforms YouTube watch URLs to embed URLs, injects the movie title, and clears iframe src on close to stop playback.

- **static/netflix/style.css**
  - Global styling and UI polish:
    - Subtle background color and base font.
    - Movie card hover animation with scale and shadow transitions.
    - Branded gradient buttons (danger/success/primary) with hover effects and shadows.
    - Styled form inputs with focus highlights (aligned with brand color).
    - Rounded cards and modal components for a modern look.
    - Navbar brand typography tweaks.
  - These styles provide a cohesive, responsive, and polished UI on top of Bootstrap.

- **static/images/default.jpg**
  - Default poster image used as a fallback when a movie has no uploaded poster.

Note: manage.py and default WSGI/ASGI files are standard scaffolding and not customized beyond the settings/urls changes listed above.

## How to Run Locally

Prerequisites
- Python 3.10+ and pip
- Django 5 (this project was scaffolded with Django 5.2.4)
- Pillow (required for ImageField)
- Git (optional, for cloning)

Setup
1) Clone and create a virtual environment
- git clone https://github.com/matin1385-tech/netflix-project.git
- cd netflix-project
- python -m venv venv
- source venv/bin/activate (Windows: venv\Scripts\activate)

2) Install dependencies
- If requirements.txt exists: pip install -r requirements.txt
- Otherwise: pip install "Django==5.2.4" Pillow

3) Database and media config
- Ensure finalproject/settings.py includes:
  - INSTALLED_APPS = [..., "netflix"]
  - STATIC_URL = "static/"
  - MEDIA_URL = "/media/"
  - MEDIA_ROOT = BASE_DIR / "media"
- Apply migrations:
  - python manage.py makemigrations
  - python manage.py migrate

4) Create a superuser (to add movies/actors/directors via /admin)
- python manage.py createsuperuser

5) Run the development server
- python manage.py runserver
- Visit http://127.0.0.1:8000

6) Seed some content
- Log into /admin and create Actors, Directors, and Movies.
- Upload posters (ImageField) or rely on the default image at static/images/default.jpg.

### Setup
```bash
git clone https://github.com/matin1385-tech/netflix-project.git
cd netflix-project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install "Django==5.2.4" Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Visit: http://127.0.0.1:8000

## Features

- Authentication: Register, Login, Logout with CSRF-protected forms and Django messages.
- Movie catalog: Titles with year, genre, description, IMDb rating, actors, and directors.
- Posters and media: Poster upload with ImageField and default fallback image.
- Watchlist: Add/remove movies; "My Watchlist" page for authenticated users.
- Trailers: Bootstrap modal with JavaScript to embed YouTube trailers and stop playback when hidden.
- Responsive UI: Bootstrap 5 + custom CSS for layout and components.
- Admin: Customized admin for Movie with list_display and search.

## Data Model (summary)

- Actor: name, birth_year (nullable).
- Director: name, birth_year (nullable).
- Movie: title, description, poster, year, genre, trailer_url, imdb_rating.
  - ManyToMany to Actor and to Director.
- Watchlist: user (FK), movie (FK).
  - Views enforce uniqueness via get_or_create; consider a DB-level UniqueConstraint for robustness.

## Routes

- GET / - Home; list all movies.
- GET /movie/<int:movie_id>/ - Movie detail page.
- GET /watchlist/ - User's watchlist (login required).
- GET /watchlist/add/<int:movie_id>/ - Add to watchlist (login required).
- GET /watchlist/remove/<int:movie_id>/ - Remove from watchlist (login required).
- GET/POST /register/ - User registration.
- GET/POST /login/ - User login.
- GET /logout/ - User logout.
- GET /admin/ - Django admin site.

## Security and Performance Notes

- CSRF protection for forms; @login_required guards all watchlist actions.
- Messages framework used to display auth errors.
- Media served by Django in development; for production, use a proper static/media server (e.g., Nginx + WhiteNoise/S3).

## Limitations and Future Work

- No search/filter/sort yet; index lists all movies.
- No pagination; suitable for small datasets.
- Watchlist uniqueness currently enforced in view logic; add DB-level UniqueConstraint for robustness.
- No user ratings or recommendations; IMDb rating is display-only.
- Admin: consider registering Actor and Director models for easier content management.
- Production topics (CDN for media, S3 storage, HTTPS, rate limiting) are out of scope.

## Video Demonstration

[Watch Demo on YouTube](https://youtu.be/n6Yn52e9qjY?si=aI5oNl1EitG-aNSg)

## How This Differs from Prior CS50 Web Projects

Unlike Wiki (flat pages), Commerce (listings/bids), Mail (API + JS mail client), or Network (social posts), this app focuses on media cataloging and consumption:
- Rich data shape: two many-to-many relations (actors, directors) plus a join model for per-user watchlists.
- Media pipeline and UI: Image uploads (ImageField) and a trailer modal with dynamic JS behavior.
- Personalized experience: Auth-bound watchlist and conditional UI behavior.
These choices require orchestrating models, authentication, forms, templates, static/media handling, and admin configuration beyond the scope of earlier assignments.

## Acknowledgements

- Bootstrap 5 via CDN for styling and modals.
- Django documentation for forms/auth/media.
- Default poster image (static/images/default.jpg) is a project asset.

## Example requirements.txt

- Django==5.2.4
- Pillow>=10
