from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UserForm, ProfileForm


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(request, "accounts/login.html")


def logout_view(request):

    logout(request)

    return redirect("home")


@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html"
    )


@login_required
def edit_profile(request):

    user_form = UserForm(instance=request.user)

    profile_form = ProfileForm(instance=request.user.userprofile)

    if request.method == "POST":

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.userprofile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()

            profile_form.save()

            return redirect("profile")

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )