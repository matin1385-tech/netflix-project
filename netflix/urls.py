from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("watchlist/add/<int:movie_id>/", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist/remove/<int:movie_id>/", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)