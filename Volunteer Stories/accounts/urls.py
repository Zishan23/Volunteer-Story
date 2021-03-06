from django.contrib.auth.decorators import login_required
from django.urls import path

from accounts import views

urlpatterns = [
    path(
        "accounts/register/", views.AuthorCreateView.as_view(), name="accounts_register"
    ),
    path(
        "accounts/profile/",
        login_required(views.AuthorUpdateView.as_view()),
        name="accounts_update",
    ),
    path("about-us", views.about_us_view, name="about_us"),
    path("our-team", views.our_team_view, name="our_team"),
    path("join-us", views.join_us_view, name="join_as_volunteer"),
]
