from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Watchlist
from .forms import RegisterForm, LoginForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "netflix/index.html", {"movies": movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "netflix/movie_detail.html", {"movie": movie})

@login_required
def watchlist(request):
    user_watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, "netflix/watchlist.html", {"watchlist": user_watchlist})

@login_required
def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    Watchlist.objects.get_or_create(user=request.user, movie=movie)
    return redirect("watchlist")

@login_required
def remove_from_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    Watchlist.objects.filter(user=request.user, movie=movie).delete()
    return redirect("watchlist")

# Register
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "netflix/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, "netflix/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    return redirect("index")