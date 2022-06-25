from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.views import LoginView


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "front/index.html")

    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        print(username)
        password = request.POST["password"]
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "front/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "front/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def search(request):
    # TODO: parse query in JS to have this format
    query_input = request.POST["query_input"]
    search_parameters = request.POST["search_parameters"]
    # TODO: Do request to DBs
    return HttpResponse(f"query input:{query_input}     search parameters:{search_parameters}")