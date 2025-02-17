from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.utils.timezone import now
from django.conf import settings
from .forms import UserRegisterForm
import time

failed_attempts = {}


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Ensure hashing
            user.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome")
            return redirect("welcome")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


def user_login(request):
    global failed_attempts
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        next_url = request.GET.get("next", "welcome")

        if username in failed_attempts and failed_attempts[username]["count"] >= 5:
            time_diff = now() - failed_attempts[username]["last_attempt"]
            if time_diff.seconds < 300:
                messages.error(request, "Too many failed attempts. Try again later.")
                return redirect("login")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            failed_attempts.pop(username, None)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect(next_url)
        else:
            if username not in failed_attempts:
                failed_attempts[username] = {"count": 1, "last_attempt": now()}
            else:
                failed_attempts[username]["count"] += 1
                failed_attempts[username]["last_attempt"] = now()

            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "users/login.html")


def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return render(request, "users/logout.html")
